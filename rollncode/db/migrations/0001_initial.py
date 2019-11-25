# Generated by Django 2.2.7 on 2019-11-25 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('date_birth', models.DateField(verbose_name='Дата Рождения')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Выберете пол', max_length=6)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('genre', models.CharField(choices=[('comedy', 'Comedy'), ('tragedy', 'Tragedy'), ('drama', 'Drama'), ('adventure', 'Adventure'), ('history', 'History'), ("children's", "Children's"), ('crime', 'Crime'), ('fantasy', 'Fantasy'), ('mystery', 'Mystery'), ('horror', 'Horror'), ('thriller', 'Thriller')], default='Выберете жанр', max_length=20)),
                ('isbn_code', models.CharField(default='Введите код ISBN', max_length=20)),
                ('create_date', models.CharField(max_length=4)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Author')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]