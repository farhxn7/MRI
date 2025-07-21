from django.shortcuts import render,redirect
from user.models import UserRegister
from user.forms import User_Reg_Form

import numpy as np
from django.core.files.storage import FileSystemStorage

# Create your views here.

#RENDERING THE BASE PAGE

def index(request):
    return render(request, 'base.html')

#RENDERING INTO ADMIN PAGE

def Admin_base(request):
    return render(request, 'admintemp/adminbase.html')

#RENDERING INTO ADMIN LOGIN PAGE
def Admin_login(request):
    if request.method=='POST':
            user =request.POST.get('username')
            passw = request.POST.get('password')
            if user=='admin' and passw == 'admin' :
                return render(request, 'admintemp/adminbase.html')
            else:
                a='check username and password'
                return render(request, 'adminlogin.html' ,{'a': a})
    else:
     return render(request, 'adminlogin.html' , {})
  
def RegisterUsersView(request):
    data = UserRegister.objects.all()
    return render(request,'admintemp/viewregisteruser.html',{'data':data})

def Activate(request):
    if request.method =='GET':
        id=request.GET.get('uid')
        status = 'activated'
        UserRegister.objects.filter(id=id).update(status=status)
        data = UserRegister.objects.all()
        return render(request, 'admintemp/viewregisteruser.html', {'data':data})
    
def Deleteuser(request):
    if request.method =='GET':
        id = request.GET.get('uid')
        UserRegister.objects.filter(id=id).delete()
        data =UserRegister.objects.all()
        return render (request, 'admintemp/viewregisteruser.html',{'data' : data})
 
#RENDERING INTO USERBASE PAGE

def User_Base(request):
    return render(request, 'usertemp/userbase.html')

#RENDERING INTO USERREGISTER PAGE
def User_register(request):
    forms = User_Reg_Form()
    if request.method=='POST':
            form =User_Reg_Form(request.POST, request.FILES)
            if form.is_valid():
              print('datasaved sucessfully---')
              form.save()
              return redirect('userlogin')
            else:
             print('data not saved')
             return redirect('userregister')

    context = {
        'forms' : forms
    }
    return render(request, 'userregister.html', context)
#RENDERING INTO USERLOGIN PAGE
def User_Login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('usrname is:', username,'password is',password)
        try:
            check=UserRegister.objects.get(username=username, password=password)
            status = check.status
            if status=='activated':
                request.session['id']=check.id
                request.session['logeduser']=check.name
                request.session['username'] =username
                request.session['email'] = check.email
                print('user id at',check.id , status)

                return render(request, 'usertemp/userbase.html',{})
            else:
                print("login error")
        except Exception as e:
            print('Exception as', str(e))
            a =  "User is not authorised by admin "
            return render(request, 'userlogin.html',{'a' : a})
         
    return render(request, 'userlogin.html')
def logout(request):
    request.session.clear()
    return render(request, 'base.html')

#READING THE USER H5 PATH FOR PROCESSING
result1=''
def uploaded(request):
    from django.conf import settings
   
    if request.method=='POST':
          fille = request.FILES['hpath']
          print('THE PATH OF THE FILE IS :',fille)
          fs = FileSystemStorage()
          filename = fs.save(fille.name, fille)
          uploaded_file_url = settings.MEDIA_ROOT+'//'+filename
          print("path",uploaded_file_url)
          from user.utility.uti import read_scan, predect
          import  tensorflow as tf
          result = read_scan(uploaded_file_url)
          a=predect(uploaded_file_url)
          return render(request , 'usertemp/result.html', {'a':a})
    else:
        return render(request, 'usertemp/predection.html')
   
def prediction_Result(request):
#    pass
    from user.utility.uti import read_scan, predect
    from tensorflow.keras.models import load_model
    a=load_model('static\images\my_model.h5')   
    if a !='' :
        print("Nothing is there")
    else:
         data=predect(a)
    return render(request, 'usertemp/result.html', {'data':data})


def dataset(request):
    from django.conf import settings
    import pandas as pd
    path ="static/dataset/train.csv"
    d= pd.read_csv(path)
    if not d.empty:
            d=d.iloc[:, : -1]
    else:
            print('something error')
    print(d)
    return render(request,'usertemp/dataset.html', {'d' :d})
           
 


