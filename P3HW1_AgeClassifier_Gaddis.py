# CTI-110 
# P3HW1 - Age Classifier
# Shannon Gaddis
# March 6, 2018




# if elif else statement

def main():
    getMaturity = int (input('How old are you? Enter a number to represent years. '))


    if getMaturity <= 1:
        print('This person is an infant')
       # print('You must be at least one year old to use this calculator.')
    elif getMaturity >=2 and getMaturity <=12:
        print('This person is a child ')
    elif getMaturity >=13 and getMaturity <=19:
        print('This person is a teenager. ')
    else:
        print('This person is an adult. ')



    input()


main()
    
