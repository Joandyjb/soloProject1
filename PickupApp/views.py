from django.shortcuts import render, redirect

from PickupApp.models import *
import bcrypt
from django.contrib import messages



def index(request):
    return render(request,'LogandRegister.html')


def create(request):
    if request.method =='POST':
        errors = User.objects.create_validator(request.POST)
        if len(errors)> 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['Userpass']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            New_User = User.objects.create(
                first_Name = request.POST['UserFname'],
                last_Name = request.POST['UserLname'],
                age = request.POST['UserAge'],
                hometown = request.POST['UserHometown'],
                username = request.POST['UserUsername'],
                email = request.POST['UserMail'],
                password =pw_hash)
            request.session['User_id'] = New_User.id
            return redirect('/user/success')
    return redirect('/')

def userlog(request):
    return render(request, 'login.html')


def login(request):
    if request.method =='POST':
        User_with_email= User.objects.filter(email = request.POST['UserMail'])
        if User_with_email:
            user = User_with_email[0]
            if bcrypt.checkpw(request.POST['Userpass'].encode(), user.password.encode()):
                request.session['User_id'] = user.id
                return redirect('/user/success')
        messages.error(request, "Email or Password are incorrect!")
    return redirect('/')

def success(request):
    if 'User_id' not in request.session:
        return redirect('/')
    context = {
        'current_user':User.objects.get(id=request.session['User_id']),
    }
    
    return render(request,'mainPage.html', context)


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'mainPage.html', 
                { 'mapbox_access_token': mapbox_access_token })


def logout(request):
    request.session.flush()
    return redirect('/')

def edit(request, the_userInfo_id ):
    context = {
        'UserEditid' : User.objects.get(id=the_userInfo_id)
        
    }
    return render(request,'profile.html', context )
    
    
    
    
    
    
    
    
def Update(request, the_userInfo_id):  
    if request.method =='POST':   
        errors = User.objects.Edit_validator(request.POST)
        if len(errors)> 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/profile/{the_userInfo_id}')
        else:    
            
            User_with_email= User.objects.filter(email = request.POST['EUserMail'])
            if User_with_email:
                userlog = User_with_email[0]

                if len(request.POST['newpass']) > 0:
                    if bcrypt.checkpw(request.POST['oldpass'].encode(), userlog.password.encode()):
                        Password= request.POST['newpass']
                        pw_hash = bcrypt.hashpw(Password.encode(), bcrypt.gensalt()).decode()
                        userlog.Password = pw_hash
                    else:
                        messages.error(request,"Invalid Email/ Password Combination")
                        return redirect(f'/profile/edit/{UserUptadeInfo_id}')
                userlog.first_Name= request.POST['EUserFname']
                userlog.last_Name = request.POST['EUserLname']
                userlog.username = request.POST['UserUsername']
                userlog.hometown = request.POST['UserHometown']
                userlog.email = request.POST['EUserMail']
                userlog.save()
                messages.success(request, 'Profile has been Succesfully Updated!')
                return redirect(f'/profile/{the_userInfo_id}')
                # make home page saying it was updated!
    return redirect ('/')


def Allcourt (request):
    context = {
        'Usercourt' : Court.objects.all(),
        'current_user':User.objects.get(id=request.session['User_id'])
    }
    return render(request,'Allcourts.html', context )


   
def court(request, courtid):
    context = {
        'Usercourt' : Court.objects.get(id=courtid),
        'current_user':User.objects.get(id=request.session['User_id'])
    }
    return render(request,'court.html', context )

def countup(request, courtid):
    if  'user_id' not in request.session:
        courtplayer= User.objects.get(id=request.session['User_id'])
        courtplayer.courts.add(Court.objects.get(id=courtid))
        courtplayer.save()
        return redirect(f'/court/{courtid}')

    return redirect('/')


def nocount(request, courtid):
    if 'user_id' not in request.session:
        courtplayer= User.objects.get(id=request.session['User_id'])
        courtplayer.courts.remove(Court.objects.get(id=courtid))
        courtplayer.save()
        return redirect(f'/court/{courtid}')

