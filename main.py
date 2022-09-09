from life360 import Life360

def main():

    function_dict = {'get_me': life360.get_me, 'get_circles': life360.get_circles,
                    'get_code': life360.get_code, 'get_messages': life360.get_messages,
                    'get_history': life360.get_history, 'get_emergency_contacts': life360.get_emergency_contacts,
                    'set_circle': life360.set_circle, 'help': life360.help}

    while True:
        user_input = input('Enter: ')
        user_input.lower()
        if user_input in function_dict:
            print(function_dict[user_input]())
        elif user_input == 'get_circle_info':
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