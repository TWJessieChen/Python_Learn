#Craps赌博游戏

from random import randint

#Craps赌博游戏
def print_craps(): 
   money = 1000
   while money > 0:
       print('總資金:', money)
       needs_go_on = False
       while True:
           debt = int(input('請下注: '))
           if 0 < debt <= money:
               break
       first = randint(1, 6) + randint(1, 6)
       print('玩家擲出了%d點' % first)
       if first == 7 or first == 11:
           print('玩家勝!')
           money += debt
       elif first == 2 or first == 3 or first == 12:
           print('莊家勝!')
           money -= debt
       else:
           needs_go_on = True
       while needs_go_on:
           needs_go_on = False
           current = randint(1, 6) + randint(1, 6)
           print('玩家擲出了%d點' % current)
           if current == 7:
               print('莊家勝')
               money -= debt
           elif current == first:
               print('玩家勝')
               money += debt
           else:
               needs_go_on = True
   print('Game Over!!!')

# Main function
if __name__ == '__main__':
   print_craps()
