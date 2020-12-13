print("Grade system according to Canadian University")
input = int(input(" Enter the percentage: "))
if input <=49:
  print(" your grade is F ")
elif input >= 50 and input<= 54 :
  print(" your grade is D")
elif input >=55 and input<= 59:
  print (" your grade is C-")
elif input >= 60 and input<=64:
  print (" your grade is C")
elif input >=65 and input<=69:
  print(" your grade is C+")
elif input >= 70 and input<=72 :
  print (" your grade is B-")
elif input >=73 and input<=76:
  print (" your grade is B")
elif input >= 77 and input<= 79:
  print (" your grade is B+")
elif input >= 80 and input<=84:
  print (" your grade is A-")
elif input >= 85 and input<=89:
  print (" your grade is A")
else:
  print (" your grade is A+")