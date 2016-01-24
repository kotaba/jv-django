#*-* coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

Group.add_to_class('is_project', models.BooleanField(verbose_name='Группа проекта', default=False))
