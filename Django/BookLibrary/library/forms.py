from django import forms

#Simple form to get the Book name from user
class SearchBook(forms.Form):
    title = forms.CharField(label='Search a book', 
                            max_length=100, 
                            widget=forms.TextInput(attrs={'placeholder': 
                                'Enter any Book Name'}))
