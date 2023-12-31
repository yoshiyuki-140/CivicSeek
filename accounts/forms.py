from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class SignUpForm(UserCreationForm):
    '''
    UserCreationFormのサブクラス
    '''
    class Meta:
        model = UserModel
        # fields = ('name', 'birth_data', 'email', 'password','region','profession')
        fields = ('username', 'email', 'password1', 'password2')