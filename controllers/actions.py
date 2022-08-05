import abc
from abc import ABC

from controllers.factories import InstrumentSpecFactory
from models import Instrument, InstrumentType


class ActionInterface(ABC):
    @abc.abstractmethod
    def start(self):
        raise NotImplementedError('Actions must implement start method')


class ShowInstrumentsAction(ActionInterface):
    def start(self):
        Instrument.print_all_instruments()


class AddInstrumentAction(ActionInterface):
    def start(self):
        instrument_type = input('What is the instrument type?\n')
        try:
            type_enum = InstrumentType(instrument_type)
        except ValueError:
            print('Unknown instrument type!')
            return False

        try:
            price = int(input('What is the instrument price?\n'))
        except TypeError:
            print('Invalid price')
            return False

        spec = InstrumentSpecFactory(type_enum).get_instrument_spec_class()
        for prop in spec.properties:
            is_valid = False
            while not is_valid:
                property_value = input(f'Provide value for: {prop}\n')
                try:
                    setattr(spec, prop, property_value)
                    is_valid = True
                except Exception as e:
                    print(e)

        instrument = Instrument(type_enum, price, spec)
        instrument.create()
        return True


class SearchInstrumentAction(ActionInterface):
    def start(self):
        pass
