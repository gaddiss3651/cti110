# CTI-110 
# P5HW1 - Test Average and Grade
# Shannon Gaddis
# April 22, 2018


def main():

    def getScores():


        s1 = float(input("Please enter score 1: "))

 
        s2 = float(input("Please enter score 2: "))


        s3 = float(input("Please enter score 3: "))


        s4 = float(input("Please enter score 4: "))


        s5 = float(input("Please enter score 5: "))

        return s1, s2, s3, s4, s5


    s1, s2, s3, s4, s5 = getScores()
    calc_average(s1, s2, s3, s4, s5)



def determine_grade(detScore):


    if(detScore < 60):


        return "F"


    elif(detScore < 70):


        return "D"


    elif(detScore < 80):


        return "C"


    elif(detScore < 90):


        return "B"


    elif(detScore < 101):


        return "A"

def calc_average(s1, s2, s3, s4, s5):

    print ("\nScore\tGrade")
    print ("-----\t------")

    print( format(s1,',.0f') + "\t", determine_grade(s1), "\n", 
            format(s2,',.0f') + "\t", determine_grade(s2), "\n", 
            format(s3,',.0f') + "\t", determine_grade(s3), "\n", 
            format(s4,',.0f') + "\t", determine_grade(s4), "\n", 
            format(s5,',.0f') + "\t", determine_grade(s5)),"\n", 

    average = (s1 + s2 + s3 + s4 + s5) / 5

    print ("\nYour average is: ", format(average,',.0f') + ".\tYour course letter grade is: ", determine_grade(average), sep="")    


main()
