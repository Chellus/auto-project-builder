import string

MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 30

VALID_CHARS = (
    list(string.ascii_uppercase) +
    list(string.ascii_lowercase) +
    [str(x) for x in range(10)] +
    ['-', '_']
    )

def is_valid_project_name(name):
    for ch in name:
        if ch not in VALID_CHARS:
            return False

    if len(name) < MIN_NAME_LENGTH:
        return False

    if len(name) > MAX_NAME_LENGTH:
        return False

    return True

def is_valid_author(author):
    if len(author) == 0:
        return False

    return True

if __name__ == "__main__":
    project_name = input("What is your project name?\n")

    while not is_valid_project_name(project_name):
        project_name = input("Invalid project name. Try again\n")

    #if not is_valid_project_name(project_name):
    #    print("Invalid project name. Exiting")
    #    exit(0)

    author = input("Who is the author of this project?\n")

    while not is_valid_author(author):
        author = input("Invalid author. Try again\n")

    print("PROJECT DETAILS\n")
    print("Project name: ", project_name)
    print("Author: ", author)
