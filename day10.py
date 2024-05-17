print("Bill Calculator")
print("++++++++++++++++")
print()
myBill = float(input("What was the bill?: "))
tip = float(input("What percentage do you want to tip?: 5% , 10% or 15%:" ) )
if tip == 5:
  tip = myBill * 0.05
elif tip == 10:
  tip = myBill * 0.10
elif tip == 15:
  tip = myBill * 0.15
else:
  print("Invalid tip percentage")
print("Tip: ", round(tip,2))
totalByll = myBill + tip
print(round(totalByll,2))
numberOfPeople = int(input("How many people?: "))
answer = totalByll / numberOfPeople
print("You all owe", round(answer,2))