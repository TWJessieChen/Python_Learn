#Prime number 質數
#指在大於1的自然數中，除了1和該數自身外，無法被其他自然數整除的數（也可定義為只有1與該數本身兩個正因數的數）

from math import sqrt

#For in 迴圈
def print_prime_number(): 
    num = int(input('請輸入一個正整數: '))
    if(num < 0) :
        print('輸入不是正整數 %d' % num)
        return
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是質數' % num)
    else:
        print('%d不是質數' % num)

# Main function
if __name__ == '__main__':
   print_prime_number()
