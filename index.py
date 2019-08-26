#!C:\Users\gusrl\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-Type: text/html")
print()
import cgi, os

files = os.listdir('data')
print(files)
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
    <h2>{title}</h2>
    {desc}
</body>
</html>
'''.format(title=pageId,desc=description,listStr=listStr))
