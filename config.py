from os import getenv
from dotenv import load_dotenv

load_dotenv()


SESSION_NAME = AQCjdlJpzO-J30NEJR9KtcIQiQYYcGA0ZEXwkQGDjEJX4kQMQUzeWfWbqAy2Cisw_TZPvkRRWVfRddZriJJlV-pGJvc9VIhqSLaDbyXGCgl9zH_q9xAgizVqcjJ79wBRd6fe9CtlEBi8GaPZn1hBuJFsR27qMm7ySKXjX1r-e_BkHQonMSDBCxWveix1ccm9imEa6kjItIEWirUW6EeaKclHQ50bkvd_irxYdc4qPgVTeE9nlZA4SWc9q2eJ58CpBoKMKqmGEOrfMad6dYzNiqCeWrCHKSfRpbGbtwUs_Trv1o3JgtSwTrhZrDA7RFiQNcVB1jPVqsW29HMFjH5dqlTFPH0wA
BOT_TOKEN = getenv("BOT_TOKEN")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
