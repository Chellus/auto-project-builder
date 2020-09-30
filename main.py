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

def write_template_to_file(template_path, output_path, params):
    with open(template_path, 'r') as f: #open the template and write its contents into an string
        template_string = f.read()

    template = Template(template_string) #render the template into the contents variable
    contents = template.render(params)

    with open(output_path, 'w+') as f: #write contents into the output file
        f.write(contents)

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

    main_output_path = os.path.join(output_dir_path, "main.py")
    readme_output_path = os.path.join(output_dir_path, "README.md")
    todo_output_path = os.path.join(output_dir_path, "TODO.md")
    #write main.py file
    write_template_to_file(
        template_path='Templates/main.py.template',
        output_path=main_output_path,
        params={
            'project_name' : project_name
        }
    )
    print("Created main.py file at ", main_output_path)
    #write readme file
    write_template_to_file(
        template_path='Templates/README.md.template',
        output_path=readme_output_path,
        params={
            'project_name' : project_name,
            'author' : author
        }
    )
    print("Created README.md file at ", readme_output_path)
    #write todo file
    write_template_to_file(
        template_path='Templates/TODO.md.template',
        output_path=todo_output_path,
        params={
            'project_name' : project_name,
        }
    )
    print("Created TODO.md file at ", todo_output_path)

    print("PROJECT DETAILS\n")
    print("Project name: ", project_name)
    print("Author: ", author)
