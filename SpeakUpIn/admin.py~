#*-*: coding: utf-8 *-*
from django.contrib import admin
from SpeakUpIn.models import Ticket
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export import fields
# Register your models here.

class TicketResource(resources.ModelResource):
    ticket_id = fields.Field(column_name='Номер')
    full_name = fields.Field(column_name='ФИО')
    is_ticket = fields.Field(column_name='Заявка')
    phone = fields.Field(column_name='Телефон')
    age = fields.Field(column_name='Возраст')
    city = fields.Field(column_name='Город')
    stop_reason = fields.Field(column_name='Причина отказа')
    place = fields.Field(column_name='Школа')
	
    class Meta:
        model = Ticket
	exclude = ('id', 'first_name', 'last_name', 'middle_name')
	export_order = ('ticket_id', 'full_name', 'is_ticket', 'phone', 'age', 'city', 'stop_reason', 'place')
	

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
	list_filter = ['city', 'is_ticket', 'recall']
	

admin.site.register(Ticket, TicketAdmin)
