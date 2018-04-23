# CTI-110 
# Kilometer Converter
# Shannon Gaddis
# April 17, 2018


#######If you embed everything in a main, you start with a main then it doesn't matter when you call or create a function.
#######You can call a function before you actually created it as long as you call it at the bottom

CONVERSION_FACTOR = 0.6214


def main():
    #Get the distance from user in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)

def show_miles (km):
    #Calculate miles
    miles = km * CONVERSION_FACTOR

    #Display the miles
    print (format(km,',.0f'), 'kilometers equals', format(miles,',.0f'), 'miles. ')

main()



