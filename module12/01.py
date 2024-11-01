from enum import Enum

class WEEK(Enum):
    MONDAY = 1
    TUESDAY = 2

class OperatingSystem(Enum):
    UBUNTU = "linux"
    MACOS = "darwin"
    WINDOWS = "win"
    DEBIAN = "linux"

class Size(Enum):
    S = 1
    M = 2
    L = 3
    XL = 4


class UserRoles(Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    REGULAR_USER = "regular_user"


role = input("What's your role >>> ")

match role:
    case UserRoles.ADMIN.value | UserRoles.MODERATOR.value:
        print("welcome admin!")

    case UserRoles.REGULAR_USER.value:
        print("welcome regular user!")
    
    case _:
        print("You have no access to this page")



# if UserRoles.ADMIN.value == role or UserRoles.MODERATOR.value == role:
#     print("welcome to admin panel, you can change data now!")
# elif UserRoles.REGULAR_USER.value == role:
#     print("welcome regular user!")
# else:
#     print("You have no access to this page")






