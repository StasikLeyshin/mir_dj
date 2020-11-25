from django.conf import settings
from django.db import models

import os
from datetime import date
import datetime
# Create your models here.








class Topics(models.Model):
    #id = models.IntegerField(primary_key=True)
    #id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=200,
                            help_text="Введите название темы")
    soc = models.CharField("Сокращение названия", max_length=200,
                            help_text="На английском", default="")
    #image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

class Rassilka(models.Model):
    name = models.CharField("Название", max_length=200,
                            help_text="Введите название рассылки")
    text = models.TextField("Текст",
                            help_text="Введите текст рассылки (максимальная длинна сообщения в вк 4096 знаков с пробелами)")
    post = models.CharField("Пост", max_length=200,
                            help_text="Введите ссылку на пост в вк", blank=True)
    date_start = models.DateTimeField(blank=False, verbose_name="Дата и время начала")
    #date_start = models.DateField(blank=False, default=date.today(), verbose_name="Дата начала")
    #time_start = models.TimeField(blank=False, default=datetime.time(), verbose_name="Время начала")
    period = models.CharField("Период", max_length=200,
                           help_text="Пример: 1 день, 25 часов", default="1 час")
    #them = models.ForeignKey(to="Topics", on_delete=models.SET_NULL, null=True, verbose_name="Тема")
    them = models.ManyToManyField(Topics, verbose_name="Тема")
                                  # help_text="Выберете тему")
    image_1 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №1")
    image_2 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №2")
    image_3 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №3")
    image_4 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №4")
    image_5 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №5")
    image_6 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №6")
    image_7 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №7")
    image_8 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №8")
    image_9 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №9")
    image_10 = models.ImageField(upload_to="%Y/%m/%d", blank=False, default="0", verbose_name="Фото №10")
    #them = models.ManyToManyField(Topics, verbose_name="Тема",
                                  #help_text="Выберете тему")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

'''class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    token = models.CharField("Токен", max_length=200,
                            help_text="Введите токен от группы")'''

'''class Location(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Локация", default=u'')

class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    location = models.ForeignKey(Location, related_name='photos', on_delete=models.CASCADE)'''

'''def user_directory_path(instance,filename):
    base_name = os.path.basename(filename)
    name,ext = os.path.splitext(base_name)

    return "note/user/"+ str(instance.note.user.id) + "/"+ str(instance.note.id)+ "/"+"IMG_" + str(instance.note.id)+ext

class Note(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    #text = encrypt(models.TextField(null=True,blank=True))
    #tags = models.ManyToManyField(Tag)
    #created_date = models.DateTimeField(auto_now_add=True)
    #last_modified = models.DateTimeField(auto_now=True)
    #slug = models.SlugField(null=False,unique=True)
    # color =
    # pin =
    # collaborator =

    #class Meta:
        #ordering= ['-last_modified']

    #def getNoteTags(self):
        #return self.tags.all()

    def __str__(self):
        return self.title

class Image(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path,null=True,blank=True)

    def __str__(self):
        return self.note.title + " Img"'''


