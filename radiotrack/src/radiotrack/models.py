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
    manufacturer: Manufacturer
    

@dataclass
class RadioAccessory:
    id: int = field(kw_only=True)
    accessory_type: RadioAccessoryType
    accessory_model: str
    accessory_name: str
    accessory_manufacturer: Manufacturer
    cost: Decimal
    selling_price: Decimal | None = None


@dataclass
class Radio:
    id: int = field(kw_only=True)
    manufacturer: Manufacturer
    model: str
    model_number: str
    serial_number: str
    status: RadioStatus    
    cost: Decimal
    date_acquired: date
    accessories: list[RadioAccessory] = field(default=list)
    selling_price: Decimal | None = None
    
