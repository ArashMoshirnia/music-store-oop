from controllers import StoreManager

PROMPT = 'What do you want to do? 1: Show instruments, 2: Add new instrument, 3: Search instruments, -1: Exit store\n'

if __name__ == '__main__':
    user_input = input(PROMPT)
    while user_input != '-1':
        input_manager = StoreManager(user_input)
        input_manager.do_action()
        user_input = input(PROMPT)
