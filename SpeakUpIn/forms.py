#*-* coding: utf-8 *-*
from django import forms

class NewTicketForm(forms.Form):
    phone = forms.CharField(max_length=50, label="Телефон", required=True)
    first_name = forms.CharField(max_length=50, label="Имя", required=True)
    last_name = forms.CharField(max_length=50, label="Фамилия", required=False)
    middle_name = forms.CharField(max_length=50, label="Отчество", required=False)
    city = forms.CharField(max_length=10, label="Город", required=True)
    age = forms.CharField(max_length=50, label="Возраст", required=True)
    school = forms.CharField(max_length=200, label="Школа", required=True)