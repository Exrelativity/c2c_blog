# Blog

```
requirement python==3.9.0
```

# To run the project

```
source venv/bin/activate
```

```
python manage.py loaddata users.json
```

```
python3 manage.py runserver
```

## Routes for our blog

```
admin  
profile  
profile/<int:id>  
profile/<int:id>/update  
profile/<int:id>/create  
profile/<int:id>/delete  
post  
post/<int:id>  
post/<int:id>/update  
post/<int:id>/create  
post/<int:id>/delete  
auth/login   
auth/register  
auth/password/forgot  
auth/password/update  
auth/confirm/email  
```

Please note for new setup comments ### fields on the post form.py file with modelchoice as this fields courses migration errors,
after migration the field can be uncommented back.
