# Co0nditional Execution
scores = input("Enter Score: ")
score=float(scores)

if score>=0.9:
	print("A")
elif score>=0.8:
    print("B")
elif score>=0.7:
    print("C")
elif score>=0.6:
    print("D")
elif score<0.6:
    print("F")    
else:  
    print("ERROR")
    