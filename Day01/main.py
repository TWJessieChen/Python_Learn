#變數 & 型態


#變數名稱 = 變數值
def print_var(): 
    a = 321 #變數a = 整數321
    b = 12  #變數b = 整數12
    print('a + b : ' a + b)    # 333   #變數a + 變數b
    print(a - b)    # 309   #變數a - 變數b
    print(a * b)    # 3852  #變數a * 變數b
    print(a / b)    # 26.75 #變數a / 變數b

#變數型態
def print_var_type(): 
    a = 100 #整數
    b = 12.345  #浮點數
    c = 1 + 5j  #複數
    d = 'hello, world'  #字串
    e = True    #布林值
    f = None    #空值

    print(type(a))    # <class 'int'>
    print(type(b))    # <class 'float'>
    print(type(c))    # <class 'complex'> 複數，實數部分為 a，虛數部分為 b，科學計算，圖像處理，信號處理等應用領域才會使用的變數類型
    print(type(d))    # <class 'str'>
    print(type(e))    # <class 'bool'>
    print(type(f))    # <class 'NoneType'>
    


# Main function
if __name__ == '__main__':
   print_var()
   print_var_type()






