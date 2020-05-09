#build spec file
pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" app.py --path 'C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64'

#build exe
pyinstaller app.spec