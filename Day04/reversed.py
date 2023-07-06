#Reversed number

#Reversed number
def print_reversed_number(): 
   num = int(input('num = '))
   reversed_num = 0
   while num > 0:
       reversed_num = reversed_num * 10 + num % 10
       num //= 10
   print(reversed_num)

# Main function
if __name__ == '__main__':
   print_reversed_number()
