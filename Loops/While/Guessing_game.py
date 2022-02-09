Secret_Word = "Harsh"
guess = ""
guess_count = 0
Total_guess = 3
Out_of_guess = False

while guess!= Secret_Word and not(Out_of_guess):
    if guess_count < Total_guess:
        guess=input("Enter word:- ")
        guess_count +=1
        remain_guess= 3 - guess_count
        print("Remain Guesses:- " + str(remain_guess))
    else:
        Out_of_guess = True

if Out_of_guess:
    print("You lost game!")
else:
    print("You Win!")