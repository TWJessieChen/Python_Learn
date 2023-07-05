#Greatest Common Divisor and Least Common Multiple
#最大公因數和最小公倍數
#輸入兩個正整數計算它們的最大公因數和最小公倍數

#While 迴圈
def print_greatest_common_divisor_and_least_common_multiple(): 
    x = int(input('x = '))
    y = int(input('y = '))
    # 如果x大於y就交换x和y的值
    if x > y:
        # switch x and y，交换x和y的值
        x, y = y, x
    #從兩個數中較小的數開始做遞減的迴圈    
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公因數是%d' % (x, y, factor))
            print('%d和%d的最小公倍數是%d' % (x, y, x * y // factor))
            break

# Main function
if __name__ == '__main__':
   print_greatest_common_divisor_and_least_common_multiple()
