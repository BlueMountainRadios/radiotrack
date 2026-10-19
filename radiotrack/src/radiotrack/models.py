from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal


@dataclass
class RadioStatus:
    id: int
    status: str
    meaning: str


@dataclass
class Manufacturer:
    id: int = field(kw_only=True)
    name: str


@dataclass
class RadioAccessoryType:
    id: int = field(kw_only=True)
    accessory_type: str


@dataclass
class RadioAccessory:
    id: int = field(kw_only=True)
    name: str
    model: str
    accessory_type: RadioAccessoryType
    manufacturer: Manufacturer
    purchase_price: Decimal
    selling_price: Decimal | None = None


@dataclass
class Radio:
    id: int = field(kw_only=True)
    manufacturer: Manufacturer
    model: str
    model_number: str
    serial_number: str
    status: RadioStatus
    purchase_price: Decimal
    date_acquired: date
    accessories: list[RadioAccessory] = field(default=list)
    selling_price: Decimal | None = None
