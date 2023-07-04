#Conversion of grades(成績轉換)

#Conversion of grades(成績轉換)
def print_conversion_of_grades(): 
    score = float(input('輸入成績: '))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('轉換完後的等級是:', grade)
    
# Main function
if __name__ == '__main__':
   print_conversion_of_grades()

