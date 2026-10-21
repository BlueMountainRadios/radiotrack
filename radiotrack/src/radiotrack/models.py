from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class RadioStatus:
    id: int
    status: str
    meaning: str


@dataclass
class Manufacturer:
    id: int
    name: str


@dataclass
class AccessoryType:
    id: int
    type: str
    description: str


@dataclass
class Accessory:
    id: int
    name: str
    model: str
    accessory_id: AccessoryType
    manufacturer_id: Manufacturer
    purchase_price: Decimal
    selling_price: Decimal


@dataclass
class Radio:
    id: int
    manufacturer: Manufacturer
    model: str
    model_number: str
    serial_number: str
    status: RadioStatus
    purchase_price: Decimal
    date_acquired: date
    selling_price: Decimal

@dataclass
class AccessoryToRadio:
    id: int
    accessory_id: int
    radio_id: int
