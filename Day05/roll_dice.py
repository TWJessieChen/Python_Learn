#Roll dice
from random import randint

#Roll dice
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c

# Main function
if __name__ == '__main__':
   # 摇一颗色子
   print(roll_dice())
   # 摇三颗色子
   print(roll_dice(3))
   print(add())
   print(add(1))
   print(add(1, 2))
   print(add(1, 2, 3))
   print(add(c=50, a=100, b=200))
