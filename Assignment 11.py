def readposint():
    try:
        number = input("Enter a positive integer: ")

        number = int(number)

        if number > 0:
            return number
        else:
            print("That is not a positive integer.")
            return None

    except:
        print("That is not a positive integer.")
        return None


answer = readposint()

print(answer)
