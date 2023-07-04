#Calculate the area of a triangle(計算三角形面積)

#Calculate the area of a triangle(計算三角形面積)
def print_calculate_area_triangle(): 
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and a + c > b and b + c > a:
        print('周長: %f' % (a + b + c))
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('三角形面積: %f' % (area))
    else:
        print('無法構成三角形')
    
# Main function
if __name__ == '__main__':
   print_calculate_area_triangle()

