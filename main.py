from life360 import Life360

def main():

    function_dict = {'get_me': life360.get_me, 'get_circles': life360.get_circles,
                    'get_code': life360.get_code, 'get_messages': life360.get_messages,
                    'get_history': life360.get_history, 'get_emergency_contacts': life360.get_emergency_contacts,
                    'set_circle': life360.set_circle, 'help': life360.help}

    print("Start by setting the circle you want to track(set_circle).")
    print("Type: 'help' for a list of commands.")

    while True:
        user_input = input('Enter: ')
        user_input.lower()
        if user_input in function_dict:
            print(function_dict[user_input]())
        elif user_input == 'help':
            help()
        elif user_input == 'get_circle_info':
            print('control-c to break loop')
            print('beginning...')
            time.sleep(3)
            try: 
                while True:
                    print(life360.get_circle_info())
            except KeyboardInterrupt:
                print(KeyboardInterrupt)
        else:
            print('Invalid input. Try Again.')

if __name__ == '__main__':
    life360 = Life360('USER_EMAIL', 'USER_PASSWORD')
    main()