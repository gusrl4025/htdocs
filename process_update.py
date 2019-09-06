#!C:\Users\gusrl\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)

#Redirection
print("LocationL: index.py?id="+title)
print()
