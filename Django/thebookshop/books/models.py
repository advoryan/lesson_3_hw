from django.db import models

class Book(models.Model):
    name = models.CharField(
        "Название",
        null=False,
        blank=False,
        max_length=200)

    image = models.ImageField(
        "Обложка",
        upload_to='media/img/',
        null=True,
        blank=True)

    author = models.ManyToManyField(
        "data.Author",
        related_name="books",
        verbose_name="Автор")

    price = models.DecimalField(
        "Цена",
        max_digits=5,
        decimal_places=2)

    serie = models.ForeignKey(
        "data.Series",
        related_name="books",
        verbose_name="Серия",
        # null=True,
        # blank=True,
        on_delete=models.CASCADE)

    genre = models.ManyToManyField(
        "data.Genre",
        related_name="books",
        blank=True,
        verbose_name="Жанр")

    year = models.PositiveSmallIntegerField(
        "Год издания",
        null=True,
        blank=True)

    page = models.PositiveSmallIntegerField(
        "Количество страниц",
        null=True,
        blank=True)

    bind = models.ForeignKey(
        "data.Binding",
        verbose_name="Переплет",
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    book_format = models.ForeignKey(
        "data.BookFormat",
        verbose_name="Формат",
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    isbn = models.CharField(
        "ISBN",
        default="0",
        unique=True,
        max_length=20)

    weight = models.PositiveSmallIntegerField(
        "Вес, гр",
        null=True,
        blank=True, )

    age_limit = models.PositiveSmallIntegerField(
        "Возрастные ограничения",
        null=True,
        blank=True,)

    publish = models.ForeignKey(
        "data.Publish",
        verbose_name="Издательство",
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    book_amount = models.PositiveIntegerField(
        "Кол-во книг в наличии",
        default=0)

    available = models.BooleanField(
        "Доступна для заказа",
        default=True)

    rate = models.FloatField(
        "Рейтинг",
        default=0)

    created_day = models.DateTimeField(
        "Дата внесения в каталог",
        auto_now=False,
        auto_now_add=True)

    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        permissions = [('edit-content', 'for content-managers'), ('edit-order', 'for edit-managers'), ('market', 'for marketers')]
