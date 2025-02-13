from decouple import config
from logic import guess_the_number

capital = int(config("CAPITAL"))
min_number = int(config("MIN_NUMBER"))
max_number = int(config("MAX_NUMBER"))
attempts = int(config("ATTEMPTS"))

guess_the_number(capital, min_number, max_number, attempts)
