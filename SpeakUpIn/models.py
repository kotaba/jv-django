#*-*: coding: utf-8 *-*
from __future__ import unicode_literals

from django.db import models

class Ticket(models.Model):

    REASON_CHOICES = (
    	('Не интересно', 'Не интересно'),
    	('2', 'Изучает в другой школе'),
    	('3', 'Отлично изучил'),
    	('4', 'Находится не в Украине',),
	('5', 'В другом городе',),
	)

    SCHOOL_CHOICES = (
	('Выбор Школы', 'Выбрать Школу'),
    	('г. Киев м. Минская, Оболонский проспект 6', 'г. Киев м. Минская, Оболонский проспект 6'),
    	('г. Одесса ул. Ришельевская 6Б', 'г. Одесса ул. Ришельевская 6Б'),
	)

    first_name = models.CharField(max_length=50, blank=True, verbose_name='Имя')
    is_ticket = models.BooleanField(default=False, blank=True, verbose_name='Заявка')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    phone = models.IntegerField(blank=False, verbose_name='Телефон')
    city = models.CharField(max_length=30,  blank=True, verbose_name='Город')
    age = models.IntegerField(blank=True, null=True, verbose_name='Возраст')
    place = models.CharField(max_length=200,  blank=True, verbose_name='Школа')
    stop_reason = models.CharField(max_length=200, choices=REASON_CHOICES, blank=True, verbose_name='Причина Отказа')
    recall = models.BooleanField(default=False, blank=True, verbose_name='Перезвон')
    recall_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата перезвона')
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    owner = models.CharField(max_length=200, verbose_name='Специалист', null=True)

    class Meta:
        app_label = 'SpeakUpIn'
        permissions = (
            ("view_project", "Can see project"),
            ("add_ticket", "Can add tickets"),
        )

    def getFullName(self):
        return "%s %s %s" % (self.last_name, self.first_name, self.middle_name)
    getFullName.admin_order_field = 'last_name'
    getFullName.short_description = "ФИО"

    def __unicode__(self):
        return "Номер телефона: %s, ФИО: %s %s %s, %s" % (self.phone,
                                                      self.last_name,
                                                      self.first_name,
                                                      self.middle_name,
                                                      self.city)
