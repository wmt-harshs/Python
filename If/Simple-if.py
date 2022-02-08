
Is_male = False           #input("Is you male:- ")
Is_tall = False         #input("Is you tall:- ")

if Is_male and Is_tall:
    print("You are tall male.")

elif Is_male and not(Is_tall):  
    print("You are short male.")

elif not(Is_male) and Is_tall:  
    print("You are not male but you are tall.")

else:
    print("You are nither male nor tall.")
    