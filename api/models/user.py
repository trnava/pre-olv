from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.timezone import now

from api.models.sex import Sex
from api.models.genre import Genre


class UserManager(BaseUserManager):
    """ User manager """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """ Create and save a user """
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, editable=False)
    email = models.EmailField('email', unique=True)
    is_staff = models.BooleanField('is_staff', default=False)
    is_active = models.BooleanField('is_active', default=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class UserDetail(models.Model):
    """
    type:
        0 =  default
        1 = buyer
        2 = artist
        3 = both
    """

    """ common """
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.IntegerField(default=0, blank=True)
    icon = models.ImageField(default='icons/default.jpg', blank=True, upload_to='icons/')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    """ BUYER INFORMATION """
    ready_as_buyer = models.BooleanField(default=False)
    last_name = models.CharField(default='', blank=True, max_length=30)
    first_name = models.CharField(default='', blank=True, max_length=30)
    zipcode = models.CharField(default='', blank=True, max_length=10)
    address = models.CharField(default='', blank=True, max_length=200)
    phone_number = models.CharField(default='', blank=True, max_length=20)

    """ ARTIST INFORMATION """
    ready_as_artist = models.BooleanField(default=False, blank=True)
    debuted = models.BooleanField(default=False, blank=True)
    approved = models.IntegerField(default=0, blank=True)
    ticket = models.IntegerField(default=0, blank=True)
    artist_name = models.CharField(default='', blank=True, max_length=30)
    profile = models.TextField(default='', blank=True)
    website = models.CharField(default='', blank=True, max_length=200)
    sex = models.ForeignKey(Sex, default=0, blank=True, on_delete=models.PROTECT)
    place = models.CharField(default='', blank=True, max_length=20)
    birthday = models.DateField(null=True, blank=True)

    bank_name = models.CharField(default='', blank=True, max_length=20)
    bank_branch = models.CharField(default='', blank=True, max_length=20)
    bank_branch_code = models.CharField(default='', blank=True, max_length=20)
    bank_number = models.CharField(default='', blank=True, max_length=20)
    bank_account_name = models.CharField(default='', blank=True, max_length=20)

    def __str__(self):
        return self.user_id
#
#
# class BuyerDetail(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.PROTECT)
#     ready_to_buy = models.BooleanField(default=False)
#     name = models.CharField(max_length=40)
#     address = models.CharField(max_length=200)
#     phone_number = models.CharField(max_length=20)
#     credit_number = models.CharField(max_length=20)
#     credit_name = models.CharField(max_length=50)
#     created_at = models.DateTimeField(default=now)
#     updated_at = models.DateTimeField(default=now)
#     deleted_at = models.DateTimeField(null=True, blank=True, default=None)
#
#     def __str__(self):
#         return self.name
#
#
# class ArtistDetail(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.PROTECT)
#     debuted = models.BooleanField(default=False)
#     approved = models.IntegerField(default=0)
#     ticket = models.IntegerField(default=0)
#     ready_to_sell = models.BooleanField(default=False)
#     artist_name = models.CharField(max_length=20)
#     website = models.CharField(max_length=100)
#     sex = models.ForeignKey(Sex, null=True, on_delete=models.PROTECT)
#     genre = models.ForeignKey(Genre, null=True, on_delete=models.PROTECT)
#     birthday = models.DateField(null=True, blank=True)
#     place = models.CharField(max_length=20)
#     profile = models.TextField()
#     icon = models.CharField(max_length=200, null=True, blank=True)
#     account = models.CharField(max_length=10)
#     account_branch = models.CharField(max_length=10)
#     account_name = models.CharField(max_length=30)
#     account_number = models.CharField(max_length=10)
#     created_at = models.DateTimeField(default=now)
#     updated_at = models.DateTimeField(default=now)
#     deleted_at = models.DateTimeField(null=True, blank=True, default=None)
#
#     def __str__(self):
#         return self.artist_name
