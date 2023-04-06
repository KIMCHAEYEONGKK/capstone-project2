from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.


# GENDER_CHOICES = (
#     ("w", "여자"), ("M", "남자"),
# )

# EXERCISE_EVERYDAY = "every"
# EXERCISE_ONCE = "one"
# EXERCISE_THREE = "three"
# EXERCISE_FOUR = "four"
# EXERCISE_NO = "no"
#
# EXERCISE_CHOICES = (
#     (EXERCISE_EVERYDAY, '일주일에 운동을 매일 합니다.'),
#     (EXERCISE_FOUR, '일주일에 4~5번합니다.'),
#     (EXERCISE_THREE, '일주일에 3~4번합니다.'),
#     (EXERCISE_ONCE, '일주일에 1~2번합니다.'),
#     (EXERCISE_NO, '일주일에 운동을 안합니다.')
# )


class CommonManager(BaseUserManager):
    def create_user(self, name, username, gender,age, tall, exercise,password=None):
        if not name:
            raise ValueError('must have user name')
        if not username:
            raise ValueError("must have userID.")
        user = self.model(
            name=name,
            username=username,
            age=age,
            tall=tall,
            gender=gender,
            exercise=exercise
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, age,tall,name,exercise,username,gender, password):
        user = self.create_user(
            username=username,
            password=password,
            name=name,
            age=age,
            tall=tall,
            gender=gender,
            exercise=exercise
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class Common(AbstractBaseUser):
    name = models.CharField(max_length=20, verbose_name='이름', default='')
    username = models.CharField(max_length=20, unique=True, default='', verbose_name="아이디")
    age = models.CharField(max_length=20, default='', verbose_name="나이")
    tall = models.CharField(max_length=20, default='', verbose_name="키")
    gender = models.CharField(max_length=20,default='',verbose_name="성별")
    exercise = models.CharField(max_length=100,default='',verbose_name="운동여부")
    # gender = models.CharField(max_length=1, verbose_name="성별", choices=GENDER_CHOICES,default='')
    # exercise = models.CharField(max_length=20, verbose_name="운동여부", choices=EXERCISE_CHOICES, default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CommonManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['name','age','tall','gender','exercise']

    def __str__(self):
        return self.username

    class Meta:
        db_table = "UserCommon"
        verbose_name = "common"

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

