#!/usr/bin/python

import sys, json

file = sys.argv[1]

with open('src/'+file) as f:
    projects = json.load(f)

initial = '''
<html>
<head>
    <title>C Projects</title>
</head>
<body>
'''

final = '''
</body>
</html>
'''

i = 0

def generate_middle(name: str, link: str, students: list) -> str:
    global i
    i += 1
    students = '\n'.join(students)
    return f'''
    <div class="project-{ i }">
        <p>
            Name of project: { name }
            <br>
            Link: { link }
            <br>
            By: { students }    <!--will need to think about using list-->
        </p>
    </div>
    '''

for_middle = [generate_middle(project['name'], project['link'], project['by'].values()) for project in projects.values()]

with open("html/c-projects.html", "w") as html_file:
    #html_file.write(initial)
    sys.stdout.write(initial)
    for each_middle in for_middle:
        #html_file.write(each_middle)
        sys.stdout.write(each_middle)
    #html_file.write(final)
    sys.stdout.write(final)
 
