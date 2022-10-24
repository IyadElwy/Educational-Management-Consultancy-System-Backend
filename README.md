# Educational Management Consultancy System Backend

### <ins>General guidelines for getting started:</ins>
###### - Create your own branch (eg. Admin_Branch) from the main branch and always work on that one
###### - Don't change or add code or files in files or folders you did not create or worked on (Conflicts in merging)
###### - Add any files that are specific to your dev process in the `.gitignore` file (eg. IDE config files)
###### - Any secret keys or variables to be added in the `Config.env` File

### <ins> Guidelines for getting started with a new feature:</ins>
###### - The `EMCS` folder is the folder with the main starting point routes, so you are only allowed to make changes in the `settings.py` file and add one root route per django app in `urls.py`
###### - Run `python manage.py startapp appName` to start a new app
###### - Add the app to the `INSTALLED_APPS` list in `settings.py` in the `EMCS` folder



### <ins>Guidelines specific for django best practices:</ins>
###### - When you run the `makemigrations` command always add the specific app name. (Eg. You made a change to the School DB model so when you migrate don't do `python manage.py makemigrations`. Instead do `python manage.py makemigrations School`)
###### - Try to write tests if you finish an entire app
###### - Always register created models to `admin.py`
###### - Always add the `to string` method for your model


