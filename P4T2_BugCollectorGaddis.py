# P4T2
# Bug Collector
# Shannon Gaddis
# March 22, 2018



#accumulator variable must start with zero
total_bugs = 0

# need 7 days
for days in range (1,8):
    print ('How many bugs did you collect on day', days)
    bugs = float(input())

    total_bugs = total_bugs + bugs

print('You collected',format(total_bugs,',.0f'), 'bugs.')

