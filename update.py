#!C:\Users\gusrl\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-Type: text/html")
print()
import cgi, os
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if "id" in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r',encoding='UTF-8').read()
else:
    pageId = 'Welcome'
    description = open('main_data/GameEngine','r',encoding='UTF-8').read()
print('''<!DOCTYPE html>
<html>
<head>
    <title>Game Engine - Hello</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href = "index.py">GameEngine</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>
'''.format(title=pageId,desc=description,listStr=listStr,form_default_title=pageId,form_default_description=description))
