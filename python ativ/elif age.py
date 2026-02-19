age = int(input("enter your age: "))
if age < 18:
    print(age, "you are a minor")
elif age < 59:
    print(age, "you are an adult")
else:
    print(age, "you are a senior")