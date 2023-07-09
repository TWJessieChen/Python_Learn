#Math function(C(M,N))

#Math function(C(M,N))
def print_math_n_m(): 
   m = int(input('m = '))
   n = int(input('n = '))
   fm = 1
   for num in range(1, m + 1):
      fm *= num
   fn = 1
   for num in range(1, n + 1):
      fn *= num
   fm_n = 1
   for num in range(1, m - n + 1):
      fm_n *= num
   print(fm // fn // fm_n) # // 整除, 直接列印

#Math function(C(M,N))
def print_math_fac(num):
    result = 1 
    for n in range(1, num + 1):
        result *= n
    return result # 回傳結果
m = int(input('m = '))
n = int(input('n = '))
print(print_math_fac(m) // print_math_fac(n) // print_math_fac(m - n)) # // 整除, 直接列印

# Main function
if __name__ == '__main__':
   print_math_n_m()
   print_math_fac(3)
