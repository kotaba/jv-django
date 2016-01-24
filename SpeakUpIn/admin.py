#*-*: coding: utf-8 *-*
from django.contrib import admin
from SpeakUpIn.models import Ticket
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export import fields
import datetime
from datetime import timedelta
import pytz
from daterange_filter.filter import DateRangeFilter
# Register your models here.

class TicketResource(resources.ModelResource):
    ticket_id = fields.Field(column_name='Номер')
    full_name = fields.Field(column_name='ФИО')
    phone = fields.Field(column_name='Телефон')
    age = fields.Field(column_name='Возраст')
    city = fields.Field(column_name='Город')
    place = fields.Field(column_name='Школа')
    owner = fields.Field(column_name='Cпециалист')
    created = fields.Field(column_name='Дата')

    class Meta:
        model = Ticket

	exclude = ('id',
               'first_name',
               'last_name',
               'middle_name',
               'is_ticket',
               'stop_reason',
               'recall_date',
               'recall',
               'creation_date')
	export_order = ('ticket_id',
                    'phone',
                    'full_name',
                    'age',
                    'city',
                    'place',
                    'owner',
                    'created')


    def dehydrate_ticket_id(self, ticket):
	return ticket.id

    def dehydrate_phone(self, ticket):
	return ticket.phone

    def dehydrate_age(self, ticket):
	return ticket.age

    def dehydrate_city(self, ticket):
	return ticket.city

    def dehydrate_place(self, ticket):
	return ticket.place

    def dehydrate_created(self, ticket):
        format = "%d.%m.%Y %H:%M"
        datetime_obj_utc = ticket.creation_date + timedelta(hours=2)
        return datetime_obj_utc.strftime(format)

    def dehydrate_owner(self, ticket):
	return ticket.owner

    def dehydrate_stop_reason(self, ticket):
	reason = ticket.stop_reason
	if reason:
		return reason
	else:
		return 'Нет'


    def dehydrate_is_ticket(self, ticket):
	is_ticket = ticket.is_ticket
	if is_ticket:
		return 'Да'
	else:
		return 'Нет'
    def dehydrate_full_name(self, ticket):
	return '%s %s %s' % (ticket.first_name.capitalize(), ticket.last_name.capitalize(), ticket.middle_name.capitalize())

class TicketAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    resource_class = TicketResource
    list_filter = [('creation_date', DateRangeFilter), 'city', 'is_ticket', 'recall', 'owner']
    list_display = ['phone', 'getFullName', 'creation_date', 'city', 'owner']
    ordering = ['-creation_date']



admin.site.register(Ticket, TicketAdmin)
