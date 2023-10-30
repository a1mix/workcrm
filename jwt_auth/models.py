from django.contrib.auth.models import AbstractUser
from django.db import models

class CrmUser(AbstractUser):
    is_not_active_reason = models.CharField(max_length=255)

    def __str__(self):
        return str(self.get_all_permissions())
