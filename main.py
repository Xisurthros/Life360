import requests, time, json

def speedProcess(speed):
        if speed < 0:
            return 0.0
        else:
            return speed

def write_json(json_data, filename="data.json"):
    with open(filename, 'w') as f:
        json.dump(json_data, f, indent=4)

def binary_string(data):
    if data == 0:
        return False
    else:
        return True

def convert(data):
    return tuple(x for x in data)

class life360:

    def __init__(self):
        self.circleID = ''
        try:
            headers = {
                'Accept': 'application/json',
                'Authorization': 'Basic U3dlcUFOQWdFVkVoVWt1cGVjcmVrYXN0ZXFhVGVXckFTV2E1dXN3MzpXMnZBV3JlY2hhUHJlZGFoVVJhZ1VYYWZyQW5hbWVqdQ==', #This code seems to change from time to time
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        
            data = 'username=YOUREMAIL&password=YOURPASSWORD&grant_type=password' #Sub your email and password
        
            response = requests.post('https://www.life360.com/v3/oauth2/token', headers=headers, data=data) #Possibly updated to v4 now

            self.access_token = response.json()['access_token']
        except json.decoder.JSONDecodeError:
            pass
    
    def get_me(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get('https://www.life360.com/v3/users/me', headers=headers)
        print(response.json())

    def get_circles(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get('https://www.life360.com/v3/circles.json', headers=headers).json()
        return response
    
    def get_code(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get(f'https://www.life360.com/v3/circles/{self.circleID}/code', headers=headers)
        print(response.json())

    def get_messages(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get(f'https://www.life360.com/v3/circles/{self.circleID}/messages', headers=headers)

        for item in response.json()['messages']:
            print(item,'\n')

    def get_history(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get(f'https://www.life360.com/v3/circles/{self.circleID}/members/history', headers=headers)
        #print(response.json())

        for item in response.json()['locations']:
            print(item, '\n')

    def get_emergency_contacts(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get(f'https://www.life360.com/v3/circles/{self.circleID}/emergencyContacts', headers=headers)
        print(response.json())

    def circle_info(self):
        print('control-c to break loop')
        print('beginning...')
        time.sleep(3)
        try:
            while True:
                headers = {
                    'Accept': 'application/json',
                    'Authorization': f'Bearer {self.access_token}',
                }
                
                response = requests.get(f'https://www.life360.com/v3/circles/{self.circleID}', headers=headers)
                data = response.json()
                group = {
                    'ID': data['id'],
                    'Group Name': data['name'],
                    'Member Count': data['memberCount'],
                    'unreadMessages': data['unreadMessages'],
                    'unreadNotification': data['unreadNotifications'],
                    'members': data['members']
                }
                for person in group['members']:

                    homies = {
                        'ID': person['id'],
                        'First': person['firstName'],
                        'Last': person['lastName'],
                        'Address1': person['location']['address1'],
                        'Address2': person['location']['address2'],
                        'Since': time.ctime(person['location']['since']),
                        'inTransit': binary_string(person['location']['inTransit']),
                        'isDriving': binary_string(person['location']['isDriving']),
                        'Speed': speedProcess(person['location']['speed']*2.23),
                        'Sharing': binary_string(person['features']['shareLocation']),
                        'Battery': person['location']['battery'],
                        'wifiState': binary_string(person['location']['wifiState']),
                        'Phone': person['loginPhone'],
                        'Email': person['loginEmail'],
                        'Latitde': person['location']['latitude'],
                        'Longitude': person['location']['longitude'],
                        'createAt': time.ctime(int(person['createdAt']))
                    }
                    print(homies, '\n\n')
        except KeyboardInterrupt:
            print(KeyboardInterrupt)

def set_circle():
    circles = life360.get_circles()['circles']
    circleData = {}
    for circle in circles:
        circleData[circle['name']] = circle['id']
    print(circleData)
    user_input = input('Enter circle name: ')
    life360.circleID = circleData[user_input]


def help():
    print('[COMMANDS]')
    print('get_me:\tInformation about account used to login.')
    print('get_circles:\tUsers circle information.')
    print('get_code:\tGet active code if any.')
    print('get_messages:\tGet all messages of the account user to login.')
    print('get_history:\tGet history of users in the circle.')
    print('get_emergency_contacts:\tGet emergency contact information of account used to login.')
    print('circle_info:\tGet current information of all users in the circle.')

def main():
    print("Start by setting the circle you want to track(set_circle).")
    print("Type: 'help' for a list of commands.")
    while True:
        user_input = input('Enter: ')
        user_input.lower()
        if user_input == 'help':
            help()
        elif user_input == 'test':
            print(life360.circle)
        elif user_input == 'set_circle':
            set_circle()
        elif user_input == 'get_me':
            life360.get_me()
        elif user_input == 'get_circles':
            print(life360.get_circles())
        elif user_input == 'get_code':
            life360.get_code()
        elif user_input == 'get_messages':
            life360.get_messages()
        elif user_input == 'get_history':
            life360.get_history()
        elif user_input == 'get_emergency_contacts':
            life360.get_emergency_contacts()
        elif user_input == 'circle_info':
            life360.circle_info()
        else:
            print('Invalid input. Try Again.')


if __name__ == '__main__':
    life360 = life360()
    main()