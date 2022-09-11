# pyLife360

**pyLife360** is a simple library to rip data from Life360's unoffical API.

## Main example:
```python
from life360 import Life360
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
```
USER_EMAIL & USER_PASSWORD must be replaced with your login information.

## Response example:
```python
>>> from pyLife360 import Life360

>>> life360 = Life360('USER_EMAIL', 'USER_PASSWORD')
>>> print(life360.me)
{'id': '000000e0-0a0a-00b0-b000-000000000000', 'firstName': 'YOUR_FIRST_NAME', 'lastName': 'YOUR_LAST_NAME', 'loginEmail': 'exmaple@email.com', 'loginPhone': '+10000000000', 'avatar': 'https://www.life360.com/img/user_images/000000e0-0a0a-00b0-b000-000000000000/00b00e00-0caa-0000-0000-000d0ea0000b.jpg?fd=2', 'locale': 'en_US', 'language': 'en', 'created': '2022-01-01 12:00:00', 'avatarAuthor': None, 'settings': {'map': {'police': '0', 'fire': '0', 'hospital': '0', 'sexOffenders': '0', 'crime': '0', 'crimeDuration': 'a', 'family': '0', 'advisor': '0', 'placeRadius': '0', 'memberRadius': '0'}, 'alerts': {'crime': '0', 'sound': '0'}, 'zendrive': None, 'locale': 'en_US', 'unitOfMeasure': 'i', 'dateFormat': 'mdy12', 'timeZone': 'America/Chicago'}, 'communications': [{'channel': 'Voice', 'value': '+10000000000', 'type': 'Home'}, {'channel': 'Email', 'value': 'exmaple@email.com', 'type': None}], 'cobranding': []}

>>> print(life360.circles)
{'circles': [{'id': 'f00000d0-b0e0-000d-0b00-000a00bf0000', 'name': 'circle0', 'color': '7f26c2', 'type': 'basic', 'createdAt': '1652100000', 'memberCount': '0', 'unreadMessages': '0', 'unreadNotifications': '0', 'features': {'ownerId': None, 'skuId': None, 'premium': '0', 'locationUpdatesLeft': 0, 'priceMonth': '0', 'priceYear': '0', 'skuTier': None}}, {'id': 'f11111d1-b1e1-111d-1b11-111a11bf1111', 'name': 'circle1', 'color': '7f26c2', 'type': 'basic', 'createdAt': '1652100000', 'memberCount': '0', 'unreadMessages': '0', 'unreadNotifications': '0', 'features': {'ownerId': None, 'skuId': None, 'premium': '0', 'locationUpdatesLeft': 0, 'priceMonth': '0', 'priceYear': '0', 'skuTier': None}}]}

>>> print(life360.help())
me:                             Information about account used to login.
circles:                        Users circle information.
code:                           Get active code if any.
messages:                       Get all messages of the account user to login.
history:                        Get history of users in the circle.
emergency_contacts:             Get emergency contact information of account used to login.
circle_data:                    Get circle data.
circle_live:                    Get current information of all users in the circle.
```

## Installing pyLife360 and Supported Versions

pyLife360 is available on PyPI:

```console
$ python -m pip install requests
```

pyLife360 officially supports Python 3.6+.

## Supported Features
- [help] - Get all commands listed below.
- [set_circle] - Set the active circle to get additional information.
- [me] - Information about account used to login.
- [circles] - Users circle information.
- [code] - Get active code if any.
- [messages] - Get all messages of the account user to login.
- [history] - Get history of users in the circle.
- [emergency_contacts] - Get emergency contact information of account used to login.
- [circle_data] - Get circle data.
- [circle_live] - Get current information of all users in the circle.

## Data that can be gathered
#### - Circles
> ID\
> Name\
> Member Count\
> Member Names & Information\
> Personal Unread Messages\
> Personal Unread Notifications\
> Emergence Contacts

#### - Members
> Life360 ID\
> First Name\
> Last Last\
> Current Address1\
> Current Address2\
> Location Since\
> inTransit\
> isDriving\
> Live Speed\
> Location Sharing\
> Battery\
> wifiState\
> Phone Number\
> Email\
> Latitde\
> Longitude\
> createdAt

## Cloning the repository
```shell
git clone https://github.com/Xisurthros/Life360.git
```