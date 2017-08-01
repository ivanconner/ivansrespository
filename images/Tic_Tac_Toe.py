#Ivan Conner's Tic Tac Toe
#Python Project
#
def introduction():
    print " "
    print "Tic Tac Toe Game" 
    print "----------------"
    print " "
    print "Directions:"
    print "Press the green run button to start."
    print "You choose each square to enter an 'x' or 'o' by typing the column"
    print "coordinate first(a, b, or c) and then the row coordinate (1,2, or 3)." 
    print "Then hit 'enter'. Examples are 'a1', 'b2', etc. Then you type a 'x' "
    print "or 'o' and hit 'enter'."
    print " " 
    print "       a      b      c    "
    print "    ______________________"
    print "    |      |      |      |"
    print " 1  |  a1  |  b1  |  c1  |"
    print "    |      |      |      |"
    print "    ----------------------"
    print "    |      |      |      |"
    print " 2  |  a2  |  b2  |  c2  |"
    print "    |      |      |      |"
    print "    ----------------------"
    print "    |      |      |      |"
    print " 3  |  a3  |  b3  |  c3  |"
    print "    |      |      |      |"
    print "    ----------------------"
    print " "
         
def game(a1,b1,c1,a2,b2,c2,a3,b3,c3,count):
    winner = []
    while (count <9):
         if(((a1!=" "and b1!=" "and c1!=" ")and(a1==b1==c1))or
            ((a2!=" "and b2!=" "and c2!=" ")and(a2==b2==c2))or
            ((a3!=" "and b3!=" "and c3!=" ")and(a3==b3==c3))or
            ((a1!=" "and a2!=" "and a3!=" ")and(a1==a2==a3))or
            ((b1!=" "and b2!=" "and b3!=" ")and(b1==b2==b3))or
            ((c1!=" "and c2!=" "and c3!=" ")and(c1==c2==c3))or
            ((a1!=" "and b2!=" "and c3!=" ")and(a1==b2==c3))or
            ((a3!=" "and b2!=" "and c1!=" ")and(a3==b2==c1))):
            
            print "The game is over! The winner is "+winner[count-1]+"!"   
            import sys; sys.exit()
            
         else:
            
            print "Enter a grid letter and number (for example, 'a1','b1'):"
            answer1 = raw_input()
            print "Enter x or o:"
            answer2 = raw_input()
            winner.append(answer2)
            if   answer1 == 'a1':
                a1=answer2
            elif answer1 == 'b1':
                b1=answer2
            elif answer1 == 'c1':
                c1=answer2
            elif answer1 == 'a2':
                a2=answer2        
            elif answer1 == 'b2':
                b2=answer2
            elif answer1 == 'c2':
                c2=answer2
            elif answer1 == 'a3':
                a3=answer2 
            elif answer1 == 'b3':
                b3=answer2        
            elif answer1 == 'c3':
                c3=answer2 
                            
            print " "
            print "        a       b       c    "
            print "    _________________________"
            print "    |       |       |       |"
            print " 1  |   "+a1+"   |   "+b1+"   |   "+c1+"   |"
            print "    |       |       |       |"
            print "    -------------------------"
            print "    |       |       |       |"
            print " 2  |   "+a2+"   |   "+b2+"   |   "+c2+"   |"
            print "    |       |       |       |"
            print "    -------------------------"
            print "    |       |       |       |"
            print " 3  |   "+a3+"   |   "+b3+"   |   "+c3+"   |"
            print "    |       |       |       |"
            print "    -------------------------"
            print " "
                       
            count += 1
            if count == 9:
                print "The game has ended in a stalemate!"  
                  
introduction()
game(" "," "," "," "," "," "," "," "," ",0)