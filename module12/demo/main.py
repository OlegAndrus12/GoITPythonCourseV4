from src.auth.login import login_user


if __name__ == "__main__":
    email = "andrus@gmail.com"
    password = '123'

    login_user(email, password)
