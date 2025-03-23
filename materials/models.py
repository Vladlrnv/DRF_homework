from django.db import models

from config import settings


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название курса', help_text='введите название курса')
    preview = models.ImageField(upload_to='materials/images', blank=True, null=True, verbose_name='превью')
    description = models.TextField(max_length=100, verbose_name='описание', help_text='добавьте описание курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name='course', verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='название урока', help_text='введите название урока')
    preview = models.ImageField(upload_to='materials/images', blank=True, null=True, verbose_name='превью')
    description = models.TextField(max_length=100, blank=True, null=True, verbose_name='описание', help_text='добавьте описание урока')
    link_to_the_video = models.URLField(max_length=150, blank=True, null=True, verbose_name='ссылка на видео', help_text='введите ссылку на видео')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, blank=True, null=True, verbose_name='course')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name='lesson', verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
