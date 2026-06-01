from pydantic import BaseModel, Field
from typing import List, Optional

class Preference(BaseModel):
    tag: Optional[str] = Field(default=None, max_length=100)
    group: Optional[str] = Field(default=None, max_length=100)
    max_price: Optional[float] = None
    min_weight: Optional[float] = None

class RecommendRequest(BaseModel):
    user_type: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = Field(default=None, ge=0, le=120)
    weight: Optional[float] = Field(default=None, ge=0, le=500)
    height: Optional[float] = Field(default=None, ge=0, le=300)
    goal: Optional[str] = None
    experience: Optional[str] = None
    preferences: Optional[List[Preference]] = Field(default_factory=list, max_length=50)
