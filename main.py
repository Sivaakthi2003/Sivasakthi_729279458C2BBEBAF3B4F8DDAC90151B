year=2024
if(year % 700==0)and(year%100==0):
  print("{0}is a leap")
elif(year% 4==0)and(year%100!=0):
  print("{0}is a leap")
else:
  print("{0}is not a leap year")