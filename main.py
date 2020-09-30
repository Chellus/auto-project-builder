import string
import os
from jinja2 import Template

MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 30

#valid chars are uppercase letter, lowercase letters, numbers and - _
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

    author = input("Who is the author of this project?\n")

    while not is_valid_author(author):
        author = input("Invalid author. Try again\n")

    #the path of the directory is going to be one above the cwd
    output_dir_path = os.path.join("..", project_name)

    try:
        os.mkdir(output_dir_path)
        print("Created project directory at %s" %output_dir_path)
    except OSError as e:
        print("Couldn't create directory: ", e)
        exit(0)

    #here we create a string with the contents of the README.md template
    with open("Templates/README.md.template", 'r') as f:
        readme_string = f.read()

    #here we turn that string into an instance of the template class, then we render it onto the readme readme_string
    #with the project name and the author
    template = Template(readme_string)
    readme = template.render({'project_name' : project_name, 'author' : author})

    #the path of the README.md file is going to be inside the output_dir_path
    readme_output_path = os.path.join(output_dir_path, "README.md")

    #here we create the README.md file and write the readme string into it
    with open(readme_output_path, 'w+') as f:
        f.write(readme)

    print("PROJECT DETAILS\n")
    print("Project name: ", project_name)
    print("Author: ", author)
