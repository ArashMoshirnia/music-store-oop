import inspect

from abc import ABC
from models.enums import InstrumentType, WoodMaterial, Manufacturer, GuitarType


class AbstractInstrumentSpec(ABC):
    def __init__(self):
        self._properties = [name for (name, value) in
                            inspect.getmembers(self.__class__, lambda member: isinstance(member, property))
                            if name != 'properties']

    def matches(self, instrument_spec):
        if not isinstance(instrument_spec, self.__class__):
            return False

        for prop in self.properties:
            if getattr(self, prop) != getattr(instrument_spec, prop):
                return False

        return True

    def print(self):
        for prop in self.properties:
            print(f'{prop}: {getattr(self, prop)}')

    def is_complete(self):
        for prop in self.properties:
            if getattr(self, prop) is None:
                return False
        return True

    @property
    def properties(self):
        return self._properties


class GuitarSpec(AbstractInstrumentSpec):
    def __init__(self):
        self._manufacturer = None
        self._string_count = None
        self._guitar_type = None
        self._wood_material = None
        super().__init__()

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        try:
            self._manufacturer = Manufacturer(value)
        except ValueError:
            raise Exception('Invalid manufacturer')

    @property
    def string_count(self):
        return self._string_count

    @string_count.setter
    def string_count(self, value):
        try:
            self._string_count = int(value)
        except TypeError:
            raise Exception('Invalid string count')

    @property
    def wood_material(self):
        return self._wood_material

    @wood_material.setter
    def wood_material(self, value: str):
        try:
            self._wood_material = WoodMaterial(value)
        except ValueError:
            raise Exception('Invalid wood material')

    @property
    def guitar_type(self):
        return self._guitar_type

    @guitar_type.setter
    def guitar_type(self, value: str):
        try:
            self._guitar_type = GuitarType(value)
        except ValueError:
            raise Exception('Invalid guitar type')


class Instrument:
    _instruments = {instrument_type: set() for instrument_type in InstrumentType}

    def __init__(self, instrument_type: InstrumentType, price: int, spec: AbstractInstrumentSpec):
        self._instrument_type = instrument_type
        self._price = price
        self._instrument_spec = spec

    def __str__(self):
        return f'{id(self)} - {self._instrument_type} - {self._price}'

    def create(self):
        if not self._instrument_spec.is_complete():
            raise Exception('Instrument spec is not completely filled')

        Instrument._instruments[self._instrument_type].add(self)

    def print(self):
        print(f'Type: {self._instrument_type.name} - Price: {self._price}')
        self._instrument_spec.print()
        print('-------------------------------')

    @classmethod
    def print_all_instruments(cls):
        for instrument_type, instrument_list in cls._instruments.items():
            if not instrument_list:
                print(f'No {instrument_type.name} is available for now')
                continue

            for instrument in instrument_list:
                instrument.print()