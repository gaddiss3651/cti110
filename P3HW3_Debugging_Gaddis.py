# CTI-110 
# P3HW1 - Age Classifier
# Shannon Gaddis
# March 6, 2018




# if elif else statement

def main():
    # This program takes a number of grade and outputs a letter grade

    # A system uses 10-point grading scale

    score = int (input('Enter score. '))
    aMinScore = 90
    bMinScore = 80
    cMinScore = 70
    dMinScore = 60

    if score >= aMinScore:
        print('Your grade is A!')

    elif score >= bMinScore:
        print('Your grade is B. ')

    elif score >= cMinScore:
        print('Your grade is C. ')        

    elif score >= dMinScore:
        print('Your grade is D. ')
        
    else:
        print('Your grade is: F.')


    input()


main()
    
