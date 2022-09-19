print("Welcome to Home page")

def isValid(number):
    print(number,type(number))
    num = -1
    try:
      num = int(number)
    except:
        print("Invalid value to convert to number")

    if(num>0 and num<=1000):
        return True
    else:
        return False

def optimze(data:list):
    """This method is used to remove invalid values(negative, greater than 1000)"""
    return list(filter(isValid,data))

itemWeights = input("Enter item weights seperated by space")
itemWeightsList = itemWeights.split()

print(optimze(itemWeightsList))

