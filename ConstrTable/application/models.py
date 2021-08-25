from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Application(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    brand = models.TextField(blank=True, verbose_name='Бренд')  # Необязательно к заполнению blank=True
    #Нужно будет сделать единицы измерения
    quantity = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='Количество')
    link = models.URLField(max_length=500, blank=True, verbose_name='Ссылка')  # Подразумевает установку Field.db_index в True.
    item = models.IntegerField(validators=[MinValueValidator(1)], blank=True, verbose_name='Артикул')
    shop = models.TextField(blank=True, verbose_name='Магазин')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')  # Обозначение когда создан объект
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')  # Показывает когда был отредактирован объект
    is_executed = models.BooleanField(default=False, verbose_name='Выполнено')  # По умолчанию позиция в заявке не выполнена
    area = models.ForeignKey('ConstructionSite', on_delete=models.PROTECT, verbose_name='Объект')
    #Загрузку фото надо будет переделать
    photo = models.ForeignKey('Photo', on_delete=models.PROTECT, null=True, verbose_name='Фото', blank=True)

    def get_absolute_url(self):
        return reverse('view_application', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


#класс с адресом площадки и номером
class ConstructionSite(models.Model):
    #переделать на геололокацию
    address = models.CharField(max_length=150, verbose_name='Адрес', db_index=True, blank=True)
    numb = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='Номер объекта')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
        ordering = ['numb']

    def get_absolute_url(self):
        return reverse('area', kwargs={"area_id": self.pk})


#Загрузка фото чека
class Photo(models.Model):
    bill = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'


# class ImageUploader(models.Model):
#     comment = models.CharField(max_length=150)
#     image = models.ImageField(upload_to='photo/%Y/%m/%d')