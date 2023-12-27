import random as rd
import time

from colors import Colors

def color_me(chars: str) -> str:
    return ''.join([f'{Colors.Back.DEFAULT}{Colors.Fore.DEFAULT}{char}'
                    if char == ' ' else
                    f'{chr(27)}[38;2;{(r := rd.randint(0, 255))};{(g := rd.randint(0, 255))};{(b := rd.randint(0, 255))}m\x1b[48;2;{r};{g};{b}m{char}'
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
    print(chr(27)+ '[9A')

# print('\033[6B')
print(f'\033[9E', end='')
# print(f'{chr(27)}[5AHello, world.')
# print()