from django.db import models
import re

class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors ={}
        if len(reqPOST['UserFname']) < 2 :
            errors['UserFname'] ='First Name should at least be 2 characters'
        if len(reqPOST['UserLname']) < 2  :
            errors['UserLname'] ='Last Name should at least be 2 characters'
        if len(reqPOST['UserAge']) < 2  :
            errors['UserAge'] ='Age should at least be 2 characters'
            #need to make must be at least 18 error
        # if (reqPOST['UserAge']) < 16 :
        #     errors['UserAgeverification'] ='You must be at least 16 years old!'
        
        if len(reqPOST['UserUsername']) < 5  :
            errors['UserUsername'] ='Username should at least be 5 characters'
        User_with_Username = User.objects.filter(username=reqPOST['UserUsername'])
        if len(User_with_Username)>= 1:
            errors['Username_Taken'] ='Sorry Username is already taken!'

        if len(reqPOST['UserHometown']) < 2  :
            errors['UserHometown'] ='Hometown should at least be 2 characters'
            #need to validate city 
        
        EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['UserMail']):
            errors['UserMail']='Email in wrong format'
        
        User_with_email = User.objects.filter(email=reqPOST['UserMail'])
        if len(User_with_email)>= 1:
            errors['Taken'] ='Email already taken'

        if len(reqPOST['Userpass']) < 8  :
            errors['Userpass'] ='Password should at least be 8 characters'
        if reqPOST['Userpass'] != reqPOST['UserconfirmPass']:
            errors['matching'] = 'Password must match'
        
        return errors

    def Edit_validator(self, reqPOST):
        errors={}
        if len(reqPOST['EUserFname']) < 2 :
            errors['EUserFnameedit'] ='First Name should at least be 2 characters'
        if len(reqPOST['EUserLname']) < 2  :
            errors['EUserLnameedit'] ='Last Name should at least be 2 characters'
        
        if len(reqPOST['UserUsername']) < 2  :
            errors['UserUsernameedit'] ='Username should at least be 2 characters'
        
        if len(reqPOST['UserHometown']) < 2  :
            errors['UserHometownedit'] ='Hometown should at least be 2 characters'

        EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['EUserMail']):
            errors['UserMail']='Email in wrong format'
        
        # User_with_email = User.objects.filter(Email=reqPOST['UserMail'])
        # if len(User_with_email)>= 1:
        #     errors['Taken'] ='Email already taken'

        if len(reqPOST['newpass']) < 8  :
            errors['newpass'] ='Password should at least be 8 characters'
        if reqPOST['newpass'] != reqPOST['newconfirmPass']:
            errors['matching'] = 'Password must match'


        return errors




class Court(models.Model):
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    link = models.TextField(null=True)
    # User = models.ManyToManyField(User, related_name='court_withuser', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class User(models.Model):
    first_Name = models.CharField(max_length=45)
    last_Name = models.CharField(max_length=45)
    age = models.IntegerField()
    hometown  = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    email = models.TextField()
    password = models.TextField(max_length=45)
    courts = models.ManyToManyField(Court, related_name='players')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

