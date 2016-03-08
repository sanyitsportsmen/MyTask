from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models


class Field(models.Model):
    field_data = JSONField(db_index=True)
