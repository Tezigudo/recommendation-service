from fastapi import APIRouter, Request
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel, ConfigDict
from typing import Any, Dict, List
from models.schema import RecommendRequest
from services.recommender import get_recommendations

# TODO: add shared-secret auth on /recommend (needs backend coordination)

router = APIRouter()


class EquipmentOptionResult(BaseModel):
    """Response schema for a single equipment option result.
    Extra fields (score, rule_applied, __debug, and all equipment data fields)
    are forwarded to the client unchanged."""
    model_config = ConfigDict(extra="allow")


@router.post("/recommend", response_model=List[EquipmentOptionResult])
async def recommend(req: RecommendRequest):
    "recommend the first 100 equipment option based on scoring"
    # Run CPU-bound ML work in a thread pool so the event loop is not blocked
    return await run_in_threadpool(get_recommendations, req)
