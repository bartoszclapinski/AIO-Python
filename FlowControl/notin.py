activity = input("What would you like to do today? ")


if "cinema" not in activity.casefold():     # casefold() is used to convert the string to lowercase
    print("But I want to go to the cinema")
