# SKGEzhil-Storage-Server

It is a simple cloud based storage server developed by SKGEzhil

It is simple to set up your own storage server with my project

# Setup

1. Clone the repository and name it as project_directory
2. Open the project with PyCharm IDE
3. Open the python interpreter and run the following commands<br>
```from storage_server import db, create_app```<br>
   ```db.create_all(app=create_app())```<br>
    
4. It will create a database ***"storage_db.sqlite"*** in the project folder
5. Create a folder named ***"storage"*** in the project directory manually
6. Now in ***'main.py'*** on ```lines 30, 43, 70, 72``` change the path to your ***'storage'*** directory location
7. Now run the program

