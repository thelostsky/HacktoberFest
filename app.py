print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "How many Guzhengs are usually playing with the orchestra?")
  print("   a) 12")
  print("   b) 3")
  print("   c) 1")
  print("   d) 24")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. You don't need that much sound"
    score -=1
  elif answer == "b":
    output = "Wrong.Too many"
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. This is the ensemble"
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "How old is Dunman High CO?")
  print("   a) 49 years' old")
  print("   b) 15 years' old")
  print("   c) 33 years' old")
  print("   d) 64 years' old")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. Dunman High CO  is not that new."
    score -=1
  elif answer == "c":
    output = "Wrong. Dunman High CO is formed earlier."
    score -=1
    
  elif answer == "d":
    output = "Wrong. That is how old the school is."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Around how many students are in CO?")
  print("   a) 150")
  print("   b) 300")
  print("   c) 100")
  print("   d) 200")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. There is more people than that"
    score -=1
  elif answer == "b":
    output = "Wrong. They don't require that much sound."
    score -=1
  elif answer == "c":
    output = "Wrong. Too less people."
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz. Great job!")
  
