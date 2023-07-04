#Circles Calculate function(圓的計算)

#Circles calculate operators(圓的計算)
def circles_calculate_operators(): 
    radius = float(input('輸入圓的半徑: '))       # input() 輸入, float() 轉換成浮點數
    perimeter = 2 * 3.1416 * radius             # 周長公式
    area = 3.1416 * radius * radius             # 面積公式
    print('周長: %.2f' % perimeter)              # %.2f 保留兩位小數 % perimeter 對應 perimeter
    print('面積: %.2f' % area)                   # %.2f 保留兩位小數 % area 對應 area

# Main function
if __name__ == '__main__':
    circles_calculate_operators()

