def validate_empty_input(fieldName):
    userinput = input(f"Enter {fieldName}:\n")
    while isEmpty(userinput):
        print(f"Please a valid input for {fieldName}\n")
        userinput = input("\n")
    return userinput


def isEmpty(value):
    return True if len(value) == 0 else False
