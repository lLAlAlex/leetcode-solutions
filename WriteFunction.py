def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 != 0:
            leap = True
        elif year % 100 == 0 and year % 400 == 0:
            leap = True
    
    return leap

print(is_leap(2200))