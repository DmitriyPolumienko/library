from django.db import models


# Create your models here.


class Author(models.Model):
    CHOISE_GENDER = (
        ('мужчина', "Мужчина"),
        ('женщина', "Женщина"),
    )

    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=40, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    date_birth = models.DateField(auto_now=False, verbose_name='Дата Рождения')
    gender = models.CharField(max_length=7, choices=CHOISE_GENDER,verbose_name='Пол')

    def __str__(self):
        return "Имя: %s; Фамилия:%s; Отчество:%s" % (self.name, self.surname, self.patronymic)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ('name', )


class Books(models.Model):
    CHOISE_GENRE = (
        ('comedy', "Comedy"),
        ('tragedy', "Tragedy"),
        ('drama', "Drama"),
        ('adventure', "Adventure"),
        ('history', "History"),
        ("children's", "Children's"),
        ('crime', "Crime"),
        ('fantasy', "Fantasy"),
        ('mystery', "Mystery"),
        ('horror', "Horror"),
        ('thriller', "Thriller"),
        ('other', "Other")
    )

    author = models.ManyToManyField(Author, verbose_name='Автор')
    title = models.CharField(max_length=40,verbose_name='Название')
    genre = models.CharField(max_length=20, choices=CHOISE_GENRE, default='',verbose_name='Жанр')
    isbn_code = models.CharField(max_length=20, default='',verbose_name='Код ISBN')
    create_date = models.CharField(max_length=4,default='',verbose_name='Дата написания')

    def __str__(self):
        return "Название: %s; ISBN:%s" % (self.title, self.isbn_code)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ('title', )
