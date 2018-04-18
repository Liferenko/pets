# -*-coding: utf-8 -*- 
#!/usr/bin/python3


def bsearch(numbers, value):
    size = len( list([numbers]) )
    low = 0
    high = size - 1

    while low <= high:
        mid = (low + high) / 2 
        
        if value == numbers[mid]:
            print( "Значение %s находится на %s месте в списке." % (value, mid) )
            return 0        
        elif value > numbers[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 1

if __name__ == '__main__':
    bsearch(7, 13)
    
