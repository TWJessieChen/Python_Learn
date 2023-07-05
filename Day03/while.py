#While 迴圈

#import random library
import random

#While 迴圈
def print_while(): 
    answer = random.randint(1, 100)
    counter = 0
    print('answer = %d' % answer)
    while True:
        counter += 1
        number = int(input('請輸入猜測的數字: '))
        if number < answer:
            print('大一點')
        elif number > answer:
            print('小一點')
        else:
            print('猜對了!')
            break
    print('總共猜了%d次' % counter)
    if counter > 7: #附加限制次數
        print('猜的次数太多了，需要努力啊！')

# Main function
if __name__ == '__main__':
   print_while()
