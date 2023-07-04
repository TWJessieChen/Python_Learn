#if else 判斷式

#if else 判斷式
def print_if_else(): 
    username = input('輸入帳號: ')
    password = input('輸入密碼: ')
    # 判斷帳號密碼是否正確  
    if username == 'admin' and password == '123456':
        print('驗證成功!')
    else:
        print('驗證失敗!')
    
# Main function
if __name__ == '__main__':
   print_if_else()

