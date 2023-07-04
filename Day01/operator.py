#Operator function(運算子函式)

# Arithmetic operators
def arithmetic_operators(): 
    a = 10          # a = 10 變數 a 被指定為 10
    b = 3           # b = 3  變數 b 被指定為 3 
    a += b          # a = a + b
    a *= a + 2      # a = a * (a + 2)
    print(a)        # 列印出結果 a = 195

# Conditional operators
def conditional_operators(): 
    flag0 = 1 == 1  # True
    flag1 = 3 > 2   # True
    flag2 = 2 < 1   # False
    flag3 = flag1 and flag2 # False，and 運算子，只有在兩個運算元都為 True 時，結果才為 True
    flag4 = flag1 or flag2  # True，or 運算子，只要其中一個運算元為 True 時，結果就為 True
    flag5 = not (1 != 2)    # False，not 運算子，如果運算元為 True，則結果為 False，否則結果為 True
    print('flag0 =', flag0)    # flag0 = True
    print('flag1 =', flag1)    # flag1 = True
    print('flag2 =', flag2)    # flag2 = False
    print('flag3 =', flag3)    # flag3 = False
    print('flag4 =', flag4)    # flag4 = True
    print('flag5 =', flag5)    # flag5 = False

# Main function
if __name__ == '__main__':
    arithmetic_operators()
    conditional_operators()


   