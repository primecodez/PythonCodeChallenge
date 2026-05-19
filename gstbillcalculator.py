a = int(input("Enter your amount:"))
amount = a
def gstamount(amount):
    return amount + (amount * 18/100)

print("Total Bill amount after gst: {:.2f}".format(gstamount(amount)))
