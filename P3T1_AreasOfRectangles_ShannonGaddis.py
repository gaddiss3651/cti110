# P3T1
# Areas Of Rectangles
# Shannon Gaddis
# March 6, 2018



# Get the dimensions of rectange 1
recLength1 = int(input('Enter the length of the first rectangle: '))
recWidth1 = int(input('Enter the width of the first rectangle: '))

# Get the dimensions of rectangle 2
recLength2 = int(input('Enter the length of the second rectangle: '))
recWidth2 = int(input('Enter the width of the second rectangle: '))

# Calculate the areas of the rectangles
recArea1 = recLength1 * recWidth1
recArea2 = recLength2 * recWidth2

# Determine the greater area
if recArea1 > recArea2:
    print('The first rectangle you entered has the greater area.')
else:
    if recArea2 > recArea1:
        print ('The second rectangle you entered has the greater area.')
    else:
        print ('Both rectangles have the same area.')
