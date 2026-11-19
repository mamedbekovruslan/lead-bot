from enum import Enum
from typing import Literal
from pydantic import Field, BaseModel

class LeadType(str, Enum):
    new_order = "new_order"
    question = "question"
    complaint = "complaint"
    spam = "spam"


class Lead(BaseModel):
    name: str | None = None
    contact: str | None = Field(None, description="телефон, email или @username")
    need: str = Field(description="что хочет клиент, 1 предложение")
    budget_rub: int | None = None
    urgency: Literal["low", "normal", "high"] = "normal"
    type: LeadType
    confidence: float = Field(ge=0, le=1, description="уверенность в разборе")