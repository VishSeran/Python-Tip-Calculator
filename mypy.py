
print("welcome to my calculator")

bill = float(input("enter your bill\n"))
tip_percentage = float(input("enter your tip percentage 10%, 15% or 20%\n"))
people = int(input("enter your number of people\n"))

tip = bill * tip_percentage / 100
tip_per_person = round(tip/people,3)

print(f"Each person should have {tip_per_person} amount of tip")