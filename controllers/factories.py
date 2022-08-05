from models import InstrumentType, GuitarSpec


class InstrumentSpecFactory:
    def __init__(self, instrument_type: InstrumentType):
        self._instrument_type = instrument_type

    def get_instrument_spec_class(self):
        if self._instrument_type == InstrumentType.GUITAR:
            return GuitarSpec()

        else:
            print('Unknown instrument type!')
