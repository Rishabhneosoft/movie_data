from django import forms
# from .models import *


# class MovieForm(forms.ModelForm):
#     class Meta:
#         model = Movie
#         fields = '__all__'
class MovieForm(forms.Form):
    file = forms.FileField()

# class UserForm(forms.Form):
#     first_name= forms.CharField(max_length=100,widget= forms.TextInput
#                            (attrs={'class':'input--style-3','placeholder':"First name"}))
#     last_name= forms.CharField(max_length=100,widget= forms.TextInput
#                            (attrs={'class':'input--style-3','placeholder':"Last name"}))
#     username= forms.CharField(max_length=100,widget= forms.TextInput
#                            (attrs={'class':'input--style-3','placeholder':"Username"}))
#     password= forms.CharField(max_length=100,widget= forms.PasswordInput
#                            (attrs={'class':'input--style-3','placeholder':"Password"}))
#     email= forms.CharField(max_length=100,widget= forms.TextInput
#                            (attrs={'class':'input--style-3','placeholder':"Email"}))

