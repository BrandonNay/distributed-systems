import os
import time
import numpy as np

os.system(r"printf '\033[2J'")
field = np.full((23, 80), " ")

for x in range(18):
    field[6][x+30] = "#"
field[5][28] = "#"
field[5][29] = "#"
field[5][48] = "#"
field[5][49] = "#"
field[2][39] = "@"

field[20][5] = "*"
field[20][39] = "~"
field[20][74] = "+"

stringy = ""
for i in range(23):
    for j in range(80):
        stringy += field[i, j]
os.system(f"echo '{stringy}'")

# for i in range(23):
#     for j in range(79):
#         os.system(f"echo -n '{field[i, j]}'")
#         if j == 78:
#             os.system(f"echo")

# x = 0
# while True:
#     # time.sleep(.1)
#     os.system(r"printf '\033[2J'") # clear
#     if x % 2 == 0:
#         os.system(r"printf '\033[32m'") # green
#         os.system("echo -n 123")
#         os.system(r"printf '\033[39m'") # default
#         os.system("echo 456")
#         os.system("echo 789")
#     else:
#         os.system("echo bungo")
#     x += 1
