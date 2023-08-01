########### Rock Paper Scissors Game using random module #############
import random
l=["rock","scissor","paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''Enter the Value For 
Game Start......
1 Yes
2 No | Exit
                 '''))
    if uc==1:
        for a in range(1,6):
            UserInput=int(input('''
1 Rock
2 Scissor
3 Paper
                                '''))
            if UserInput==1:
                uchoice="rock"
            elif UserInput==2:
                uchoice="Scissor"
            elif UserInput==3:
                uchoice="Paper"
            else:
                uchoice="Invalid"
            cchoice = random.choice(l)

            if cchoice==uchoice:
                print("Computer Value",cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1

            elif(uchoice=="rock" and cchoice=="scissor") or (uchoice=="scissor" and cchoice=="paper") or (uchoice=="paper" and cchoice=="rock"):
                print("Computer Value",cchoice)
                print("User Value",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer Value",cchoice)
                print("User Value",uchoice)
                print("Computer Win")
                ccount=ccount+1
         
        if ucount==ccount:
            print("Final Game Draw....")
            print("User Score",ucount)
            print("Computers Score",ccount)
        elif ucount>ccount:
            print("You Win The Game....")
            print("User Score",ucount)
            print("Computers Score",ccount)
        else:
            print("Computer Win The Game....")
            print("User Score",ucount)
            print("Computers Score",ccount)
        


    else:
        break




