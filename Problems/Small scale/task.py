tab = []

number = "0"

while number != ".":
    number = input()

    if number == ".":
        continue
    else:
        tab.append(float(number))

print(min(tab))
