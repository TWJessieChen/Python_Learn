#Unit conversion(單位轉換)

#unit conversion(單位轉換)
#英制單位英寸和公制單位厘米互換
def print_unit_conversion(): 
    value = float(input('輸入長度: '))
    unit = input('輸入單位: ')
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, value * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print('%f厘米 = %f英寸' % (value, value / 2.54))
    else:
        print('請確認輸入是否有效單位')
    
# Main function
if __name__ == '__main__':
   print_unit_conversion()

