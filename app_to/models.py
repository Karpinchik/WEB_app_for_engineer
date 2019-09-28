from django.db import models


class Customers(models.Model):
    
    class Meta():
        verbose_name_plural = 'Заказчики'
    
    name = models.CharField(max_length=100, verbose_name='Название')
    
    def __str__(self):
        return self.name


class Obj(models.Model):
    
    class Meta():
        verbose_name_plural = 'Объекты'

    name = models.CharField(max_length=100, verbose_name='Название')
    text = models.TextField(max_length=100, verbose_name='Текст')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    contract = models.CharField(max_length=100, verbose_name='Договор')
    repairs = models.CharField(max_length=100, verbose_name='Ремонт')
    sim = models.CharField(max_length=100, verbose_name='sim')
    phone = models.TextField(max_length=100, verbose_name='телефоны')
    date_contract = models.DateField(verbose_name='Дата')

    
    сustomer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='cust')

    def __str__(self):
        return self.name
