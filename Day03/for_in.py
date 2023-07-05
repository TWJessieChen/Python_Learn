#For in 迴圈

#for in 迴圈
#range(101)：可以用来產生0到100範圍的整数，需要注意的是取不到101。
def print_for_in_example1(): 
    sum = 0
    for x in range(101):
        sum += x
    print(sum)

#range(1, 101)：可以用来產生1到100範圍的整数，相當于前面是从0開始，到101之前结束，需要注意的是取不到101。
def print_for_in_example2(): 
    sum = 0
    for x in range(1, 101):
        sum += x
    print(sum)

#range(2, 101, 2)：可以用来產生2到100範圍的整数，相當于前面是从0開始，到101之前结束，
#但是这里是从2開始到101之前结束，其中2是每次跑一次迴圈增加的數值，即數值序列的增量。
def print_for_in_example3(): 
    sum = 0
    for x in range(2, 101, 2):
        sum += x
    print(sum)

#range(100, 0, -2)：可以用来產生100到0，其中-2是每次跑一次迴圈遞減的數值，即數值序列的減量。
def print_for_in_example4(): 
    sum = 0
    for x in range(100, 0, -2):
        sum += x
    print(sum)
    
# Main function
if __name__ == '__main__':
   print_for_in_example1()
   print_for_in_example2()
   print_for_in_example3()
   print_for_in_example4()

