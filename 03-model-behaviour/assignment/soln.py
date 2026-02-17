from pydantic import field_validator, model_validator, BaseModel, Field

# Todo : create Booking model


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @model_validator
    @property
    def total_amount(self) -> float:
        return self.rate_per_night * self.nights
