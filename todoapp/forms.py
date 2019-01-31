from django import forms

class TodoForm(forms.Form):
    texto = forms.CharField(max_length=40,
     widget=forms.TextInput(
         attrs={'class' : 'form-control',
                'placeholder' : 'Enter todo e.g. Delete actions completed', 
	            'aria-label' : 'Todo',
                'aria-describedby' : 'add-btn'}))