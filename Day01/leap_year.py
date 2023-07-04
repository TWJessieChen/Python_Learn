#Leap Year function(閏年判斷)

#Leap year operators(閏年判斷)
def leap_year_operators(): 
    year = int(input('輸入年份: '))
    is_leap = year % 4 == 0 and year % 100 != 0 or \
            year % 400 == 0
    print(is_leap)

# Main function
if __name__ == '__main__':
    leap_year_operators()

