import time
from colors import Colors

# print(f'\033[=1h', end='')
# print(f'{1:02}{'-'}*8')
for i in range(1, 20):
    # print(f'{i:02}{'-'*8}'*9, end='\n')
    print(f'{i:02}{'-'*8}', end='')
    # time.sleep(3)
    for j in range(1, 9):
        print(f'{j}{'-'*9}', end='')
    print(f' {i:02}')
    # print()
# print()
# exit(0)

# time.sleep(1)

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
# print(f'\033[0K 刪除至列尾(0K)', end='')

# ESC[J
# print(f'\033[6n❿ request cursor position(6n)', end='')
# print(f'\x1b M⓫ 往上一行(M)', end='')
# print(f'{chr(27)} 7⓬ save cursor position(7)', end='')
# print(f'\033 8⓭ restores the cursor to the last saved position(8)', end='')
# print(f'\x1b[s⓮ save cursor position(s)', end='')
# print(f'{chr(27)}[u⓯ restores the cursor to the last saved position', end='')
# print()
print(f'\x1b[20;0H', end='')
print()
print()

for i in range(99999999):
    print(f'\033[0E{i}', end='')
    # print(f'{i}', end='')
    # time.sleep(1)
    # print(f'\033[9E❼ 下移9列並至列首(9E)', end='')