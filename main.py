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
        
        response = requests.get('https://www.life360.com/v3/circles.json', headers=headers)
        print(response.json())
    
    def get_code(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get('https://www.life360.com/v3/circles/f91107d1-b4e2-418d-9b04-198a75bf3802/code', headers=headers)
        print(response.json())

    def get_messages(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get('https://www.life360.com/v3/circles/f91107d1-b4e2-418d-9b04-198a75bf3802/messages', headers=headers)

        for item in response.json()['messages']:
            print(item,'\n')

    def get_history(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get('https://www.life360.com/v3/circles/f91107d1-b4e2-418d-9b04-198a75bf3802/members/history', headers=headers)
        #print(response.json())

        for item in response.json()['locations']:
            print(item, '\n')

    def get_emergency_contacts(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        
        response = requests.get('https://www.life360.com/v3/circles/f91107d1-b4e2-418d-9b04-198a75bf3802/emergencyContacts', headers=headers)
        print(response.json())

    def circle_info(self):
            while True:
               #
                headers = {
                    'Accept': 'application/json',
                    'Authorization': f'Bearer {self.access_token}',
                }
                
                response = requests.get('https://www.life360.com/v3/circles/f91107d1-b4e2-418d-9b04-198a75bf3802', headers=headers)
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
                    print(homies)