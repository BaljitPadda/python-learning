"""
Task: Create a calculator that enables you to input weight in either kg or lbs and returns your weight in the
opposite unit.
"""

weight = float(input("Weight: "))
unit = input("Is this Lbs or Kg? ").lower()
if unit == "lbs":
    print("Weight in Kg: " + str(weight * 0.45))
elif unit == "kg":
    print("Weight in Lbs: " + str(weight * 2.205))