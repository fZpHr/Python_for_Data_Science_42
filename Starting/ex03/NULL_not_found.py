def NULL_not_found(object: any) -> int:
    if object == None:
        print("Nothing:  None " + str(type(object)))
        return 0
    elif type(object) == float and object != object:
        print("Chesse: nan " + str(type(object)))
        return 0
    elif type(object) == int and object == 0:
        print("Zero: 0 " + str(type(object)))
        return 0
    elif type(object) == str and object == "":
        print("Empty: " + str(type(object)))
        return 0
    elif type(object) == bool and object == False:
        print("Fake: False " + str(type(object)))
        return 0
    else:
        print("Type not found")
    return 1