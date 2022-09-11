from pyLife360 import Life360

def main():

    function_dict = {'me': life360.me, 'circles': life360.circles,
                    'code': life360.code, 'messages': life360.messages,
                    'circle_data': life360.circle_data, 'history': life360.history,
                    'emergency_contacts': life360.emergency_contacts, 'set_circle': life360.set_circle, 
                    'help': life360.help}

    while True:
        
        user_input = input('Enter: ')
        user_input.lower()
        if user_input in function_dict:
            print(function_dict[user_input]())
        elif user_input == 'circle_info':
            try: 
                while True:
                    print(life360.circle_info())
            except KeyboardInterrupt:
                print(KeyboardInterrupt)
        else:
            print('Invalid input. Try Again.')

if __name__ == '__main__':
    life360 = Life360('USER_EMAIL', 'USER_PASSWORD')
    main()