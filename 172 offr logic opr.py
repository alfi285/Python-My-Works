#Write a Python program to check if a person qualifies for a special offer based on the following criteria:

#Use and to check if the person has an annual income of at least $50,000 and is currently employed.
#Use not to ensure that the person does not have any unpaid debts.
#Use or to add an alternative condition that will pass if the person has a loyalty card, even if they don’t meet the income and employment criteria.
#If any of these conditions are met, print "Offer Granted!", otherwise print "No Offer".

income = 30000
is_unpaid_debt = True
is_loyality_card = False

if (is_loyality_card==True or income>=50000):

    print("Offer is granted")
else:
    print("No Offer")