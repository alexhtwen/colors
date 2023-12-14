import random as rd
import time

class Colors():
    class Fore():
        BLACK = '\x1b[30m'
        RED = '\x1b[31m'
        GREEN = '\x1b[32m'
        YELLOW = '\x1b[33m'
        BLUE = '\x1b[34m'
        MAGENTA = '\x1b[35m'
        CYAN = '\x1b[36m'
        WHITE = '\x1b[37m'
        BRIGHT_BLACK = '\x1b[90m'
        BRIGHT_RED = '\x1b[91m'
        BRIGHT_GREEN = '\x1b[92m'
        BRIGHT_YELLOW = '\x1b[93m'
        BRIGHT_BLUE = '\x1b[94m'
        BRIGHT_MAGENTA = '\x1b[95m'
        BRIGHT_CYAN = '\x1b[96m'
        BRIGHT_WHITE = '\x1b[97m'
        DEFAULT = '\x1b[39m'

    class Back():
        BLACK = '\x1b[40m'
        RED = '\x1b[41m'
        GREEN = '\x1b[42m'
        YELLOW = '\x1b[43m'
        BLUE = '\x1b[44m'
        MAGENTA = '\x1b[45m'
        CYAN = '\x1b[46m'
        WHITE = '\x1b[47m'
        BRIGHT_BLACK = '\x1b[100m'
        BRIGHT_RED = '\x1b[101m'
        BRIGHT_GREEN = '\x1b[102m'
        BRIGHT_YELLOW = '\x1b[103m'
        BRIGHT_BLUE = '\x1b[104m'
        BRIGHT_MAGENTA = '\x1b[105m'
        BRIGHT_CYAN = '\x1b[106m'
        BRIGHT_WHITE = '\x1b[107m'
        DEFAULT = '\x1b[49m'

def color_me(chars: str) -> str:
    return ''.join([f'{Colors.Back.DEFAULT}{Colors.Fore.DEFAULT}{char}'
                    if char == ' ' else
                    f'\x1b[38;2;{(r := rd.randint(0, 255))};{(g := rd.randint(0, 255))};{(b := rd.randint(0, 255))}m\x1b[48;2;{r};{g};{b}m{char}'
                    for char in chars])

print()
ends = []
ends.append('            ▇▇▇▇▇▇▇▇▇▇  ▇▇      ▇▇  ▇▇▇▇▇▇▇▇▇       ▇▇▇▇▇▇▇▇▇  ▇▇▇     ▇▇  ▇▇▇▇▇ ')
ends.append('                ▇▇      ▇▇      ▇▇  ▇▇              ▇▇         ▇▇▇▇    ▇▇  ▇▇   ▇▇ ')
ends.append('                ▇▇      ▇▇      ▇▇  ▇▇              ▇▇         ▇▇ ▇▇   ▇▇  ▇▇     ▇▇ ')
ends.append('                ▇▇      ▇▇▇▇▇▇▇▇▇▇  ▇▇▇▇▇▇▇▇▇       ▇▇▇▇▇▇▇▇▇  ▇▇  ▇▇  ▇▇  ▇▇       ▇ ')
ends.append('                ▇▇      ▇▇      ▇▇  ▇▇              ▇▇         ▇▇   ▇▇ ▇▇  ▇▇     ▇▇ ')
ends.append('                ▇▇      ▇▇      ▇▇  ▇▇              ▇▇         ▇▇    ▇▇▇▇  ▇▇   ▇▇ ')
ends.append('                ▇▇      ▇▇      ▇▇  ▇▇▇▇▇▇▇▇▇       ▇▇▇▇▇▇▇▇▇  ▇▇     ▇▇▇  ▇▇▇▇▇ ')
ends.append(' ')

LOOPS = 10
INTERVAL_SECONDS = 1

for _ in range(LOOPS):
    for end in ends:
        print(color_me(end))
    time.sleep(INTERVAL_SECONDS)
    print('\033[9A')

print('\033[6B')
print()
print('\x1b[38;2;255;124;135mHello, world')
# print('\x1b[38;2;153;137;91mHello, world')
# '\x1b[107m'