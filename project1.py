print("Welcome to quiz game")
ans=input("Do you want to start or quit , if yes say 's' if no say 'no'").lower()
if ans=="yes":
    print("Lets start")
    q1=input("what is 3+5?")
    if q1=="8" or q1=="eight":
        print("correct")
        score=1
    else:
        print("incorrect")
        score=-0.25
    q2=input("what is 2-1?")
    if q2=="1" or "one":
        print("correct")
        score+=1
    else:
        print("incorrect")
        score=-0.25
else:
    print("end")
print("toatal score is:",score)
    
      
