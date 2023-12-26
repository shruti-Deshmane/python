import random
l=["rock","scissor","paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
                 Game.start......
                 1 yes
                 2 no|exit

                 '''))
    
    if uc==1:
        for a in range(1,2):

            userInput=int(input('''
                                1 rock
                                2 scissor
                                3 paper
                                '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
        Cchoice=random.choice(l) 
        if Cchoice==uchoice:
            print("computer value ",Cchoice)
            print("user value",uchoice)
            print("game drawn")
            ucount=ucount+1
            ccount=ccount+1
        elif (uchoice=="rock"and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or(uchoice=="scissor" and Cchoice=="paper"):
           
            print("computer value ",Cchoice)
            print("user value",uchoice)
            print("you win")
            ucount=ucount+1
        else:
          print("computer value ",Cchoice)
          print("user value",uchoice)
          print("computer win")
          ccount=ccount+1
    if ucount==ccount:
        print("final game drawn")   
        print("user score",ucount)
        print("computer score",ccount)
    elif ucount>ccount:
        print("final you win the game")   
        print("user score",ucount)
        print("computer score",ccount)
    else:
        print("final computer win the game")   
        print("user score",ucount)
        print("computer score",ccount)
else:
     breakpoint



      
        
