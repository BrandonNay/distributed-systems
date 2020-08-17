import os
print("abc", end="")
os.system(r"printf '\033[32m'")
os.system("echo -n 123")
print("defg", end="")
os.system(r"printf '\033[39m'")
os.system("echo 456")
os.system("echo 789")
print("hijkl")