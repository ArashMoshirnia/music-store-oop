import abc
from abc import ABC

from controllers.factories import InstrumentSpecFactory
from models import Instrument, InstrumentType


class AbstractAction(ABC):
    @abc.abstractmethod
    def start(self):
        raise NotImplementedError('Actions must implement start method')

    @staticmethod
    def get_instrument_type_input():
        instrument_type = input('What is the instrument type?\n')
        try:
            type_enum = InstrumentType(instrument_type)
        except ValueError:
            print('Unknown instrument type!')
            return False

        return type_enum


class ShowInstrumentsAction(AbstractAction):
    def start(self):
        Instrument.print_all_instruments()


class AddInstrumentAction(AbstractAction):
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


class SearchInstrumentAction(AbstractAction):
    def start(self):
        type_enum = self.get_instrument_type_input()
        if not type_enum:
            return False

        spec = InstrumentSpecFactory(type_enum).get_instrument_spec_class()
        filters = input(f'Enter your desired filters among the following properties: \n {spec.properties}\n')
        for user_filter in filters.split(','):
            user_filter = user_filter.strip()
            prop, value = user_filter.split('=')
            if prop not in spec.properties:
                print(f'{prop} is not a valid property')
                continue
            try:
                setattr(spec, prop, value)
            except Exception as e:
                print(e)
                continue

        results = []
        for instrument in Instrument.get_instruments_by_type(type_enum):
            if instrument.instrument_spec.matches(spec):
                results.append(instrument)

        if not results:
            print('No instrument found with these properties')
        else:
            for instrument in results:
                instrument.print()
