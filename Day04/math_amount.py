#Math amount

#Math amount
def print_math_amount(): 
   for x in range(0, 20):
       for y in range(0, 33):
           z = 100 - x - y
           if 5 * x + 3 * y + z / 3 == 100:
               print('公雞: %d隻, 母雞: %d隻, 小雞: %d隻' % (x, y, z))

# Main function
if __name__ == '__main__':
   print_math_amount()
