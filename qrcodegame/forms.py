from django import forms

tailwind_class = """w-full border-2 border-ch-gray-light 
        bg-ch-gray-dark rounded-lg 
        focus:outline-ch-green-light focus:outline-0 
        focus:outline-offset-0 focus:border-2 
        focus:border-woys-purple focus:shadow-none 
        focus:ring-0 focus:shadow-0"""

class QuestionForm(forms.Form):
    answer = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': tailwind_class}))


class UserForm(forms.Form):
    slackhandle = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': tailwind_class}))
