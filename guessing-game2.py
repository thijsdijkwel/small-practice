 
binary=False                    
lonum,hinum=1,128               
 
import random as r
 
the_num=r.randint(lonum,hinum)  # computer chooses a number randomly
print("I'm thinking of a number between",lonum,"and",hinum)
 
lo=1
hi=hinum
guesses=0
 
for i in range(lonum,hinum):    
                                    
    if binary:  guess=lo+(hi-lo)//2     
    else:       guess=r.randint(lo,hi)
    print("Guess:",guess)
    guesses+=1                      
                                    
    if guess &amp;gt; the_num:
        print("Lower!")
        hi=guess                       
    elif guess &amp;lt; the_num:
        print("Higher!")
        lo=guess                       
    else: break                      
 
print("That took",guesses,"guesses")
