"""counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")"""

print("Fill-in the blank Lyrics!")
print("(type in the blank lyrics, see if you're as cool as me)")
print()
counter = 0
answer = "give"
while True:
    print("Never going to ____ you up")
    resp = str(input())
    counter = counter + 1
    if answer == resp:
        break
    else:
        print("Nope, try again.")
print("Well done, it only took you", counter, " attempts!")