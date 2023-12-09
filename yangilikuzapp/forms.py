from django import forms
from .models import contact
from django.contrib.auth.models import User

#CommentForm

# class CommentForm(forms.ModelForm):
#     content = forms.CharField(widget=forms.Textarea(attrs={
#         'rows': '4',
#     }))

#     class Meta:
#         model = Comment
#         fields = ('content',)

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"

class userregistrationform(forms.ModelForm):
    password1 = forms.CharField(label='parol',widget=forms.PasswordInput)
    password2 = forms.CharField(label="parolni takrolang",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","first_name","email"]


    def cleanpassword(self):
        data = self.cleaned_data
        if data["password1"] != data["password2"]:
            raise forms.ValidationError('Ikkala parol bir biriga mos kelmayapti')
        return data['password2']

