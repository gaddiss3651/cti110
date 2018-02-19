# P2HW2
# Tip Tax Total
# Shannon Gaddis
# February 18, 2018


print('Welcome to the night out tax and tip calculator', '!', sep='' )




foodCost = float(input("\nPlease enter the charge for the food: $"))

tipAmount = foodCost * 0.18
salesTax = foodCost * 0.07
purchaseTotal = foodCost + salesTax
totalCost = foodCost + tipAmount + salesTax

print('\n$',format(foodCost,',.2f'),'\tFood' , sep='')
print('$',format(salesTax,',.2f'),'\tSales Tax (7%)' , sep='')
print('______')
print('$',format(purchaseTotal,',.2f') ,'\tPurchase Total', sep='')


print('\n\nGratuity = 18% of ', format(foodCost,',.2f'), '  ($',format(tipAmount,',.2f'),')' , sep='')

print('\n\nTOTAL:')
print('\n$',format(foodCost,',.2f'),'\tPurchases' , sep='')
print('$',format(salesTax,',.2f'),'\tSales Tax (7%)' , sep='')
print('$',format(tipAmount,',.2f'),'\tGratutity (18%)' , sep='')
print('______')
print('\n$',format(totalCost,',.2f') ,'\tTOTAL COST\n\n', sep='')









