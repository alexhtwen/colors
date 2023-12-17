from datetime import datetime, timedelta
import time
from colors import Colors

COUNT_DOWN_SECS = 20
print(f'\033[?25l', end='')
for i in range(1, 20):
    print(f'{i:02}{'-'*8}', end='')
    for j in range(1, 9):
        print(f'{j}{'-'*9}', end='')
    print(f' {i:02}')

print(f'{Colors.Back.BRIGHT_CYAN}{Colors.Fore.RED}', end='')
# ❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿ ⓫ ⓬ ⓭ ⓮ ⓯ ⓰ ⓱ ⓲ ⓳ ⓴
print(f'\033[1H❶ 至第1列第1欄(H)', end='')
print(f'\x1b[12;30H❷ 至第12列第30欄(12;30H)', end='')
print(f'{chr(27)}[7A❸ 上移7列(7A)', end='')
print(f'\033[2B❹ 下移2列(2B)', end='')
print(f'\x1b[3C❺ 右移3欄(3C)', end='')
print(f'{chr(27)}[60D❻ 左移60欄(60D)', end='')
print(f'\033[9E❼ 下移9列並至列首(9E)', end='')
print(f'\x1b[1F❽ 上移1列並至列首(1F)', end='')
print(f'{chr(27)}[33G❾ 平移至同列第33欄(33G)', end='')
# print(f'\033[3M❿ 上移1列(M)', end='')
print(f'{Colors.Back.DEFAULT}{Colors.Fore.BRIGHT_GREEN}', end='')
print(f'\033[0K❿ 刪除至列尾(0K)', end='')

print(f'{Colors.Back.BLUE}{Colors.Fore.BRIGHT_YELLOW}', end='')
print(f'\x1b[18;45H', end='')
# for i in range(9999999):
#     print(f'\033[0E{i:7}   {datetime.datetime.now().strftime(format='%Y-%m-%d %H:%M:%S')}', end='')


COUNT_DOWN_SECS = 21
stop_time = datetime.now() + timedelta(seconds=COUNT_DOWN_SECS)
while (now := datetime.now()) < stop_time:
    # time.sleep(0.9)
    print(f'{(stop_time - now).seconds:3} \033[4D', end='')


# ESC[J
# print(f'\033[6n❿ request cursor position(6n)', end='')
# print(f'\x1b M⓫ 往上一行(M)', end='')
# print(f'{chr(27)} 7⓬ save cursor position(7)', end='')
# print(f'\033 8⓭ restores the cursor to the last saved position(8)', end='')
# print(f'\x1b[s⓮ save cursor position(s)', end='')
# print(f'{chr(27)}[u⓯ restores the cursor to the last saved position', end='')
# print()
print(f'\x1b[20;0H', end='')
# print()
# print()

# now = datetime.datetime.now()
# for i in range(9999999):
#     print(f'\033[0E{i:7}   {datetime.datetime.now().strftime(format='%Y-%m-%d %H:%M:%S')}', end='')
print('\x1b[?25h', end='')