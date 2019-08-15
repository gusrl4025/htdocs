#!C:\Users\gusrl\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
if "id" in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r',encoding='utf8').read()
else:
    pageId = 'Welcome'
    description = open('data/GameEngine','r',encoding='utf8').read()
print(pageId)
print('''<!DOCTYPE html>
<html>
<head>
    <title>Game Engine - Hello</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href = "index.py">GameEngine</a></h1>
    <ol>
        <li><a href = "index.py?id=Unity">Unity</a></li>
        <li><a href = "index.py?id=Unreal">Unreal</a></li>
        <li><a href = "index.py?id=Cocos2d">Cocos2d</a></li>
    </ol>
    <h2>{title}</h2>
    {desc}
</body>
</html>
'''.format(title=pageId,desc=description))