from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from enum import Enum


class RadioCondition(Enum):
    NEW = "New"
    GOOD = "Good"
    FAIR = "Fair"
    PARTS_ONLY = "Parts Only"
    UNREPAIRABLE = "Unrepairable"


class RadioStatus(Enum):
    INTAKE = "Intake"
    TESTED = "Tested"
    LISTED = "Listed"
    SOLD = "Sold"


@dataclass
class Radio:
    id: int = field(kw_only=True)
    manufacturer: str
    model: str
    model_number: str
    serial_number: str
    condition: RadioCondition
    status: RadioStatus = RadioStatus.INTAKE
    cost: Decimal
    date_acquired: date
    asking_price: Decimal
