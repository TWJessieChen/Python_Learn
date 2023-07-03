#Circles Calculate function(圓的計算)

#Circles calculate operators(溫度轉換)
def circles_calculate_operators(): 
    radius = float(input('輸入圓的半徑: '))
    perimeter = 2 * 3.1416 * radius
    area = 3.1416 * radius * radius
    print('周長: %.2f' % perimeter)
    print('面積: %.2f' % area)

# Main function
if __name__ == '__main__':
    circles_calculate_operators()

