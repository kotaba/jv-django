#*-* coding: utf-8 *-*
from django import forms

class NewTicketForm(forms.Form):

    SCHOOLS = (
       ("1",("КИЕВ Метро Житомирская - проспект Победы, 136, 3-й этаж.ТЦ VMB.")),
       ("2",("КИЕВ Метро Контрактовая площадь - ул. Спасская, 5, 2-й этаж")),
       ("3",("КИЕВ Метро Печерская - бул. Леси Украинки 26, 9 этаж.")),
        ("4",("КИЕВ Метро Позняки ул. А.Мишуги, 8 2 эт.")),
        ("5",("КИЕВ Метро Голосеевская – ул. Васильковская, 14. БЦ Стенд, 1 этаж.")),
        ("6",("КИЕВ Соломенская площадь -  БЦ Нест, ул. Урицкого, 45, 1-й этаж")),
        ("7",("КИЕВ Метро Минская  - Dreamtown,  Оболонский проспект, 1-Б")),
        (u"8",("ОДЕССА ул. Ришельевская 14, 5-й этаж")),
        ("9",("КИЕВ Метро Троещина - ул. Маяковского, 68, 2 этаж")),
        ("10",("КИЕВ Метро Университет - ул. Михаила Коцюбинского 14")),

   )

    phone = forms.CharField(max_length=50, label="Телефон", required=True)
    first_name = forms.CharField(max_length=50, label="Имя", required=True)
    last_name = forms.CharField(max_length=50, label="Фамилия", required=False)
    middle_name = forms.CharField(max_length=50, label="Отчество", required=False)
    city = forms.CharField(max_length=10, label="Город", required=True)
    age = forms.CharField(max_length=50, label="Возраст", required=True)
    school = forms.CharField(max_length=50, label="Школа", required=True)