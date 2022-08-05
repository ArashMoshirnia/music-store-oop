from enum import Enum


class InstrumentType(Enum):
    GUITAR = 'guitar'


class WoodMaterial(Enum):
    ROSEWOOD = 'rosewood'
    MAPLE = 'maple'


class StringType(Enum):
    STEEL = 'steel'
    NYLON = 'nylon'


class GuitarType(Enum):
    ACOUSTIC = 'acoustic'
    CLASSIC = 'classic'
    ELECTRIC = 'electric'


class Manufacturer(Enum):
    YAMAHA = 'yamaha'
    FENDER = 'fender'
    GIBSON = 'gibson'
