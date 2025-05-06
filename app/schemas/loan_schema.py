from pydantic import BaseModel, Field
from typing import Literal


class LoanRequestSchema(BaseModel):
    requested_amount: float = Field(..., gt=0, example=40000)


class LoanResponseSchema(BaseModel):
    decision: Literal['Approved', 'Declined', 'Undecided']
