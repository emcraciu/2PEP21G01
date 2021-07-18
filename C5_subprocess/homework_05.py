"""
Create a class for an object that can get the latest stable version of python by downloading and looking in the
content of this page: https://en.wikipedia.org/wiki/History_of_Python
To download the page try using the following command for windows
powershell -c "Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python' -OutFile 'C:\temp\page.html'"
or curl, wget, or some other tools you may have in case of mac.

Compare the retrieved version with the first 2 digits of your installed version and show a message to the user
with current and available version

"""
