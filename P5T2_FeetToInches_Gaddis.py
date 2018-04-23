# CTI-110 
# P5T2_FeetToInches 
# Shannon Gaddis
# April 17, 2018


#######If you embed everything in a main, you start with a main then it doesn't matter when you call or create a function.
#######You can call a function before you actually created it as long as you call it at the bottom

#Constant for the number of inches per foot.
INCHES_PER_FOOT = 12


def main():

#Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    #Convert inches
    print(format(feet,',.0f'), 'feet equals', format(feet_to_inches(feet),',.0f'), 'inches. ')

#function converts feet to inches.
def feet_to_inches (feet):
    #Calculate feet
    return feet * INCHES_PER_FOOT

#Call the main function    
main()



