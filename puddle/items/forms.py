from django import forms
from .models import Item

INPUT_VAR = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image')
        widgets = {'category': forms.Select(attrs={'class':INPUT_VAR}),
                   'name': forms.TextInput(attrs={'class':INPUT_VAR}),
                   'description': forms.Textarea(attrs={'class': INPUT_VAR}),
                   'price': forms.TextInput(attrs={'class': INPUT_VAR}),
                   'image': forms.FileInput(attrs={'class': INPUT_VAR}),


                   }