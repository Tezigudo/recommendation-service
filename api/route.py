from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from models.schema import RecommendRequest
from services.recommender import get_recommendations
import config

router = APIRouter()


async def verify_internal_token(x_internal_token: Optional[str] = Header(default=None)):
    """Lock /recommend to internal callers (the Go backend) when INTERNAL_TOKEN
    is configured. If it's unset (local dev) the check is skipped, so this is
    opt-in and never breaks a local run. The backend sends the matching secret
    as the X-Internal-Token header (its RECOMMENDER_INTERNAL_TOKEN)."""
    if config.INTERNAL_TOKEN and x_internal_token != config.INTERNAL_TOKEN:
        raise HTTPException(status_code=401, detail="invalid or missing internal token")


class EquipmentOptionResult(BaseModel):
    """Response schema for a single equipment option result.
    Extra fields (score, rule_applied, __debug, and all equipment data fields)
    are forwarded to the client unchanged."""
    model_config = ConfigDict(extra="allow")


@router.post("/recommend", response_model=List[EquipmentOptionResult], dependencies=[Depends(verify_internal_token)])
async def recommend(req: RecommendRequest):
    "recommend the first 100 equipment option based on scoring"
    # Run CPU-bound ML work in a thread pool so the event loop is not blocked
    return await run_in_threadpool(get_recommendations, req)
