#變數 & 型態


#變數名稱 = 變數值
def print_var(): 
    a = 321
    b = 12
    print(a + b)    # 333
    print(a - b)    # 309
    print(a * b)    # 3852
    print(a / b)    # 26.75

#變數型態
def print_type(): 
    a = 100
    b = 12.345
    c = 1 + 5j
    d = 'hello, world'
    e = True
    f = None
    print(type(a))    # <class 'int'>
    print(type(b))    # <class 'float'>
    print(type(c))    # <class 'complex'> 複數，實數部分為 a，虛數部分為 b，科學計算，圖像處理，信號處理等應用領域才會使用的變數類型
    print(type(d))    # <class 'str'>
    print(type(e))    # <class 'bool'>
    print(type(f))    # <class 'NoneType'>
    


# Main function
if __name__ == '__main__':
   print_var()
   print_type()






