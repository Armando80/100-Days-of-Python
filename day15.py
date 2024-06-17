#animal = input("What animal do you want? :")
animals = {
    "Cow": "moo",
    "Sheep": "baar",
    "Hamster": "ts ts",
    "Dog": "guau guau"}
answer = ""
while answer != "Yes":
    animal = input("What animal do you want? :")
    def getAnimal(animal):
        return animals.get(animal,0)
    print( "A",animal,"goes",getAnimal(animal))
    answer = input("Do you want to exit? : ")