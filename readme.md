#build spec file
pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" app.py --path 'C:\Program Files (x86)\Windows Kits\10\Redist\10.0.19041.0\ucrt\DLLs\x64'

#build exe
add to path:
C:\Users\lukap\AppData\Roaming\Python\Python39\Scripts
C:\Users\lukap\AppData\Roaming\Python\Python39\site-packages

run in cmdL
pyinstaller app.spec


use python 3.9