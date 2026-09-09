credit_score=int(input("Enter your cibil score:"))
if credit_score>=300 and credit_score<580:
    print("Your cibil score is poor")
elif credit_score<670:
    print("Your cibil score is fair")
elif credit_score<740:
    print("Your cibil score is good")
elif credit_score<800:
    print("Your cibil score is very good")
elif credit_score<=850:
    print("Your cibil score is excellent")
else:
    print("Your cibil score is very poor")