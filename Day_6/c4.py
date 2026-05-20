inp = str(input("Enter whatever you want:"))

list = ['mango','banana','chocolate']
list.append(inp)

def data_check(list):
    first_datatype = type(list[0])

    for item in list:
       if type(item) != first_datatype :
          print("Different data type")
          return

    print("All data in the given list is of same type")

data_check(list)