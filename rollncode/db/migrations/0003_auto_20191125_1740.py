# Generated by Django 2.2.7 on 2019-11-25 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20191125_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('мужчина', 'Мужчина'), ('женщина', 'Женщина')], default='Выберете пол', max_length=6),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='books',
            name='create_date',
            field=models.CharField(default='', max_length=4, verbose_name='Дата написания'),
        ),
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(choices=[('comedy', 'Comedy'), ('tragedy', 'Tragedy'), ('drama', 'Drama'), ('adventure', 'Adventure'), ('history', 'History'), ("children's", "Children's"), ('crime', 'Crime'), ('fantasy', 'Fantasy'), ('mystery', 'Mystery'), ('horror', 'Horror'), ('thriller', 'Thriller')], default='', max_length=20, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='books',
            name='isbn_code',
            field=models.CharField(default='', max_length=20, verbose_name='Код ISBN'),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
    ]
