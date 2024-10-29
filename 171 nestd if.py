#Write a Python program to determine if a person is eligible to obtain a driver's license based on the following criteria:

#First, check if the applicant's age is valid (between 16 and 100).
#If the age is valid, check the following conditions:
#If the applicant is 18 years old or older, print "Eligible for a driver's license."
#If the applicant is between 16 and 17 years old, check if they have completed a driver's education course:
#If they have completed the course, print "Eligible for a driver's license."
#If they have not completed the course, print "Not eligible for a driver's license. Must complete driver's education."
#If the age is not valid, print "Invalid age."


age = 16
completed_drivers_education_course = True

if age > 16 and age < 100:
    if age >= 18:
        print("Eligible for driving licenses")
    elif (16<=age>=17) and completed_drivers_education_course==True:
        print("Eligible for a driver's license")
    #else:print("pls..complete driver's education course")
else:
    print("Not eligible for driver's license, Must complete driver's education.")