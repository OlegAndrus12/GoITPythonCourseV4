# from mocker.users.fake_user import get_mocked_user
from mocker import get_mocked_user

import argparse
import json



parser = argparse.ArgumentParser(description="User data generator")
parser.add_argument("--filename", help="JSON file", required=True)
parser.add_argument("--amount", required=True)

arguments = parser.parse_args()
print(arguments)
my_arg = vars(arguments)

dict()
arguments.__dict__
vars(arguments)

print(my_arg)

filename = my_arg.get("filename")
amount = int(my_arg.get("amount"))

with open(filename, "w") as file:
    mocked_users = list()
    for i in range(amount):
        mocked_users.append(get_mocked_user())
    json.dump(mocked_users, file)
