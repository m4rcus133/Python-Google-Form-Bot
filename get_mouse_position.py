import pyautogui
import keyboard

print(f'Press ESC to get mouse current position')
keyboard.wait('esc')
x, y = pyautogui.position()
print(f'[{x},{y}]')

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
    print(day)
    for x in range(0,4):
        print(f'{x} :', end=" ")
        keyboard.wait('esc')
        x, y = pyautogui.position()
        print(f'[{x},{y}]')

# while True:
# print(f'x, y: [{x},{y}]')
# mouse position
# email =  [661,587] [691,586]

# Monday
# 0 : [837,266]
# 1 : [950,262]
# 2 : [1069,267]
# 3 : [1183,264]
# Tuesday
# 0 : [836,321]
# 1 : [951,317]
# 2 : [1068,318]
# 3 : [1192,313]
# Wednesday
# 0 : [835,377]
# 1 : [954,375]
# 2 : [1065,379]
# 3 : [1186,376]
# Thursday
# 0 : [837,430]
# 1 : [956,428]
# 2 : [1068,434]
# 3 : [1197,430]
# Friday
# 0 : [838,486]
# 1 : [954,482]
# 2 : [1072,484]
# 3 : [1190,484]


# item to discuss [664,233]

# Allergies ...
# option 1 : [666,376]
# option 2 : [665,456]
# option 3 : [666,494]
# option 4 : [663,532]
# option 5 : [666,574]
# option 6 : [665,615]
# Other  : [666,657]
# Other (fill) : [760,654]

# Any other comment : [660,804]


