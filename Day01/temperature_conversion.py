#Temperature conversion function(溫度轉換，華氏轉攝氏)

# Temperature conversion operators(溫度轉換)
def temperature_conversion_operators(): 
    f = float(input('輸入華氏温度: '))          # input() 輸入, float() 轉換成浮點數
    c = (f - 32) / 1.8                        # 華氏轉攝氏公式
    print('%.1f華氏度 = %.1f攝氏度' % (f, c))   # %.1f 保留一位小數 % (f, c) 依序對應 f, c

# Main function
if __name__ == '__main__':
    temperature_conversion_operators()

