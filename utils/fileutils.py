def appendLine(fileName, text):
    """Opens file defined by fileName parameter (this can be a name of a file or a path to it)
    And writes string defined by text parameter. Adds sing of new line on the end of passed string.
    """
    with open(fileName, "a") as myfile:
        myfile.write(text + "\n")


def appendComment(filename, comment):
    commentPrefix = "# "
    commentWithPrefix = commentPrefix + comment
    appendLine(filename, commentWithPrefix)
