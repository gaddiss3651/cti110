# CTI-110 
# P4HW1 Distance Traveled
# Shannon Gaddis
# March 25, 2018


def main():
    getDistance = int(input('What is the speed of the vehicle in MPH? '))
    hours = int(input('How many hours has the vehicle traveled? '))

    print("\nHour \t Distance Traveled")

    print("----- \t--------------------")

    for num in range (1,hours+1,1):    
        getHours = num
        Distance = getHours * getDistance

        print(num ,'\t\t',format((Distance),',.0f'),' Miles', sep='')

    input()

main()    












