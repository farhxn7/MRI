from django  import forms
from user.models import UserRegister

class User_Reg_Form(forms.ModelForm):
    
    name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control','pattern': '[a-zA-Z]+'})), required=True, max_length=100)

    username =forms.CharField(widget=(forms.TextInput(attrs={'class' : 'form-control', 'pattern': '[a-zA-Z]+'})),required=True, max_length=100)

    password =forms.CharField(widget=(forms.PasswordInput(attrs={'class' : 'form-control','pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                                                                 'title': 'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'})),required=True, max_length=100)
    
    email = forms.CharField(widget=(forms.TextInput(attrs={'class' : 'form-control','pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'})),required=True,max_length=100)

    moblie_no=forms.CharField(widget=(forms.TextInput(attrs={'class' : 'form-control','pattern': '[56789][0-9]{9}'})),required=True, max_length=100)

    address  =forms.CharField(widget=(forms.TextInput(attrs={'class' : 'form-control','rows': 4, 'cols': 22})),required=True, max_length=100)

    locality = forms.CharField(widget=(forms.TextInput(attrs={'class' : 'form-control'})), required=True, max_length=100)

    city = forms.CharField(widget=(forms.TextInput(attrs={'class': ' form-control','autocomplete' : 'off','pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '})), required=True, max_length=100)

    state = forms.CharField(widget=(forms.TextInput(attrs={'class' : 'form-control','autocomplete' : 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '})), required=True, max_length=100)

    status =forms.CharField(widget=(forms.HiddenInput()), initial='waiting', max_length=100)
           
    class Meta:
      model = UserRegister
      fields = ['name','username','password','email','moblie_no','address','locality','city','state','status',]   

  
    