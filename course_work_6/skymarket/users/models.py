from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .managers import UserManager


class UserRoles(models.TextChoices):
	USER = "user"
	ADMIN = "admin"


class User(AbstractBaseUser):
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=150, null=True)
	phone = models.CharField(max_length=20, null=True)
	email = models.EmailField(unique=True, max_length=50)
	password = models.CharField(max_length=200)
	role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER, null=True)
	image = models.ImageField(upload_to='user_avatars/', null=True)
	is_active = models.BooleanField(null=True, default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

	objects = UserManager()

	@property
	def is_admin(self):
		return self.role == UserRoles.ADMIN

	@property
	def is_user(self):
		return self.role == UserRoles.USER

	@property
	def is_superuser(self):
		return self.is_admin

	@property
	def is_staff(self):
		return self.is_admin

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return self.is_admin

	class Meta:
		verbose_name = "Пользователь"
		verbose_name_plural = "Пользователи"
		ordering = ("id",)

	def __str__(self):
		return self.email
