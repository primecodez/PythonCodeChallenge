hour = int(input("Enter the number of hours you work :"))
wageperhour = int(input("Enter the wage you earn per hour:"))

def dailywage(hour, wageperhour):
    return hour * wageperhour

print(f"For working {hour} hours you would get Rs:" , dailywage(hour, wageperhour))
