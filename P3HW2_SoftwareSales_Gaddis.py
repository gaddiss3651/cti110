# CTI-110 
# P3HW2 - Software Sales
# Shannon Gaddis
# March 6, 2018




# if elif else statement

def main():
    getPurchase = int (input('How many packages did you purchase? '))
    packageCost = 99
    dis10 = packageCost * .10
    dis20 = packageCost * .20
    dis30 = packageCost * .30
    dis40 = packageCost * .40
    getDiscount = packageCost * getPurchase

    if getPurchase < 10:
        print('Sorry no discount applies to your purchases. You need to purchase a minimum of 10 packages')

    elif getPurchase >=10 and getPurchase <=19:
        print('You have earned a 10% discount ')
        print('\n$',format((dis10 * getPurchase),',.2f'),'\tYour Discount' , sep='')
        print('$',format(getDiscount,',.2f'),'\tPackage Cost' , sep='')
        print('______')
        print('$',format(((getPurchase * packageCost) - (dis10 * getPurchase)) ,',.2f') ,'\tPurchase Total', sep='')
        
    elif getPurchase >=20 and getPurchase <=49:
        print('You have earned a 20% discount ')
        print('\n$',format((dis20 * getPurchase),',.2f'),'\t\tYour Discount' , sep='')
        print('$',format(getDiscount,',.2f'),'\tPackage Cost' , sep='')
        print('______')
        print('$',format(((getPurchase * packageCost) - (dis20 * getPurchase)) ,',.2f') ,'\tPurchase Total', sep='')

    elif getPurchase >=50 and getPurchase <=99:
        print('You have earned a 30% discount ')
        print('\n$',format((dis30 * getPurchase),',.2f'),'\tYour Discount' , sep='')
        print('$',format(getDiscount,',.2f'),'\tPackage Cost' , sep='')
        print('______')
        print('$',format(((getPurchase * packageCost) - (dis30 * getPurchase)) ,',.2f') ,'\tPurchase Total', sep='')
        
    else:
        print('You have earned a 40% discount ')
        print('\n$',format((dis40 * getPurchase),',.2f'),'\tYour Discount' , sep='')
        print('$',format(getDiscount,',.2f'),'\tPackage Cost' , sep='')
        print('______')
        print('$',format(((getPurchase * packageCost) - (dis40 * getPurchase)) ,',.2f') ,'\tPurchase Total', sep='')


    input()


main()
    
