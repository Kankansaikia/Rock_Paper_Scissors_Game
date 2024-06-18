import random
computer=random.choice([1,2,3])

yourDict={"r":1, "s":2 ,"p":3}
reverseDict={1:"Rock",2:"Scissors",3:"Paper"}

print('''Enter r for Rock.
Enter s for scissors.
Enter p for paper.''')

yourinput=input("Enter your choice: \n")
if(yourinput!="r" or "s" or "p"):
    print("Enter valid input")


your_choice=yourDict[yourinput]
print("You chose: ",reverseDict[yourDict[yourinput]],"\nComputer chose: ",reverseDict[computer])

if(computer==your_choice):
    print("It's a draw!")

else:
    if(computer==1 and your_choice==2):
        print("You Lose")

    elif(computer==1 and your_choice==3):
        print("You Win")

    elif(computer==2 and your_choice==1):
        print("You Win")
    
    elif(computer==2 and your_choice==3):
        print("You Lose")
    
    elif(computer==3 and your_choice==1):
        print("You Lose")

    else:
        print("You Win")


    