# Generated by Django 2.2.7 on 2019-11-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20191125_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('name',), 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ('title',), 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('мужчина', 'Мужчина'), ('женщина', 'Женщина')], default='Выберете пол', max_length=7),
        ),
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(to='db.Author', verbose_name='Автор'),
        ),
    ]
