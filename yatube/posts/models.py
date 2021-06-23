from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey('Group', on_delete=models.PROTECT,
                              verbose_name='Сообщество', blank=True, null=True,
                              related_name='groups')
    # PROTECT как раз сохраняет запись при удалении связей.
    # Вот если бы был CASCADE...
    published = models.BooleanField(default=True, verbose_name='Опубликованно')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date']


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщества'
        verbose_name_plural = 'Сообщества'
