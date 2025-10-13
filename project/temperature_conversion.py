unit = input("Enter unit(C / F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 2)
    print(f"that temperature in fahrenheit: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"that temperature in Celsius: {temp}°C")
else:
    print(f"unit {unit} is invalid")