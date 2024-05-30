exam = str(input("What is the name of test?: "))
maxPoints = int(input("maximum score they could you receive?: "))
yourPoints = float(input("how many points you received?: "))
percentage = float((yourPoints / maxPoints)*100)
if percentage > 89:
    grade = str("A+ 😎")
elif percentage > 79 and percentage < 90:
    grade = str("A 👌")
elif percentage > 69 and percentage < 80:
    grade = str("B 👍")
elif percentage > 59 and percentage < 70:
    grade = str("C ✔")
elif percentage > 49 and percentage < 60:
    grade = str("D 😒")
elif percentage < 50:
    grade = str("U 🤦‍♂️")
else:
    grade = str("not approving!")
print()
print("\033[34mExam Grade Calculator")
print()
print("Name of exam: ", "\033[31m",exam)
print()
print("\033[34mMax. Possible Score: ", "\033[31m",maxPoints)
print()
print("\033[34mYour score: ", "\033[31m",yourPoints)
print()
print("\033[34mYou got", round(percentage,2),"% which is a ", grade)