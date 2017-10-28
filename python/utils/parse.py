def parseArguments(listOfArguments):
    """Parse list of arguments to map"""
    lenght = len(listOfArguments)
    result = {}
    for i in range(1, lenght, 2):
        key = listOfArguments[i]
        value = listOfArguments[i + 1]
        if not key.startswith("-"):
            raise AttributeError("A key must start with '-'")

        key = key.partition("-")[2]  # removes the '-' from the argument
        result[key] = value

    return result
