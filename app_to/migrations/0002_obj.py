# Generated by Django 2.0.5 on 2019-09-17 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_to', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', models.TextField(max_length=100, verbose_name='Текст')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('contract', models.CharField(max_length=100, verbose_name='Договор')),
                ('status_to', models.CharField(max_length=100, verbose_name='Статус ТО')),
                ('repairs', models.CharField(max_length=100, verbose_name='Ремонт')),
                ('sim', models.CharField(max_length=100, verbose_name='sim')),
                ('phone', models.TextField(max_length=100, verbose_name='телефоны')),
                ('date_contract', models.DateField(verbose_name='Дата')),
                ('file_contract', models.FileField(upload_to='', verbose_name='файл договор')),
                ('file_schedule', models.FileField(upload_to='', verbose_name='файл график')),
                ('file_defect', models.ImageField(upload_to='', verbose_name='файл дефект')),
                ('сustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_to.Customers')),
            ],
            options={
                'verbose_name_plural': 'Объекты',
            },
        ),
    ]