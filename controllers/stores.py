from enum import Enum

from controllers.actions import ShowInstrumentsAction, AddInstrumentAction, SearchInstrumentAction


class UserChoice(Enum):
    show_instruments = 1
    add_instrument = 2
    search_instrument = 3

    @property
    def manager(self):
        mapper = {
            UserChoice.show_instruments: ShowInstrumentsAction,
            UserChoice.add_instrument: AddInstrumentAction,
            UserChoice.search_instrument: SearchInstrumentAction,
        }

        return mapper[self]


class StoreManager:
    def __init__(self, user_choice: str):
        self._user_choice = user_choice

    def do_action(self):
        try:
            user_choice_enum = UserChoice(int(self._user_choice))
        except ValueError:
            print('Unknown choice!')
            return False

        manager = user_choice_enum.manager()
        manager.start()
