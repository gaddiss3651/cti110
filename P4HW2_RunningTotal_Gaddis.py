# CTI-110 
# P4HW2 Running Total
# Shannon Gaddis
# March 25, 2018


def main():
    total = 0
    count = 0

    getNum = float (input ('Enter any positive number: '))

    while getNum >= 0: 
        total = total + getNum
    
        count = count +1

        getNum = float (input('Enter any positive number: '))

    print('Total: ', format((total),',.0f'))

    input()

main()












