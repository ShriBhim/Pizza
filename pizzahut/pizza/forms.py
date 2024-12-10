from django.db import models
from django import forms
from .models import Pizza

#class PizzaForm(forms.Form): #formclass
#   topping1 = forms.CharField(label='Topping1',max_length=100 , widget=forms.PasswordInput)
#   topping2 = forms.CharField(label='Topping2',max_length=100 ,widget=forms.Textarea)
# size = forms.ChoiceField(label='size',choices=[('small','small'),
#                                             ('medium','medium'),
#                                            ('large','large')])

class PizzaForm(forms.ModelForm): #django model form
    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels = {'topping1':'Topping1','size':'Size'}
#       widegets = {'topping':forms.PasswordInput()
#                 'topping2:forms.Textarea()}
class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2,max_value=10)