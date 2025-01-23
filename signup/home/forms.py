from django.forms import ModelForm
from .models import User, UserProfile, UserPost

class editForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class editFormTwo(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['city', 'age']

class editFormPost(ModelForm):
    class Meta:
        model = UserPost
        fields = ['post']