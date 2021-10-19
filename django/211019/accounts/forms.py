# User 커스텀 했기 때문에 forms도 커스텀
from django.contrib.auth.forms import(
    UserCreationForm,
)
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fileds = UserCreationForm.Meta.fields
        