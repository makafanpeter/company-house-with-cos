import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str = Field(
        description="Main address line",
        example="22nd Bunker Hill Avenue",
    )
    city: str = Field(
        description="City",
        example="Hamburg",
    )
    region: str = Field(
        description="State, province and/or region",
        example="Mordor",
    )
    post_code: str = Field(
        description="Postal code",
        example="19823",
    )

    country: str = Field(
        description="Postal code",
        example="19823",
    )


class Company(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field()
    company_number: str = Field()
    address: Address = Field()
    type_and_rating: str = Field(),
    route: str = Field(),
    industries: list = Field()
    type: str = Field()
    jurisdiction: str = Field()
    status: str = Field()
    incorporated_on: datetime = Field()
    created_at: datetime = Field(default_factory=datetime.now, alias="created_at")
    #updated_at: Optional[datetime]
