from django.db import models
from django.contrib.auth.models import AbstractUser

# abstractuser와 abstractbaseuser의 차이점은 
# abstractuser는 username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined를 기본으로 가지고 있고, 
# abstractbaseuser는 password, last_login, is_superuser, username을 기본으로 가지고 있습니다.
# 초급자에게 권하는 방법은 abstractuser를 사용하는 것입니다. abstractbaseuser는 너무 많은 것을 구현해야 하기 때문입니다.


class User(AbstractUser):
    intro = models.TextField(blank=True)
    profile_img = models.ImageField(blank=True, upload_to='user/images')