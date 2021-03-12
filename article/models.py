from django.conf import settings
from django.db import models
#from django.utils.safestring import mark_safe
from django.utils.html import mark_safe

import os
from datetime import date
import datetime
import requests
import aiohttp
import asyncio
import ujson
# Create your models here.



async def fet_post(**dat):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://127.0.0.1:5000?", json=dat) as response:
            #data = await response.read()
            d = await response.json(loads=ujson.loads)
            #d = 1
            return d




class Topics(models.Model):
    #id = models.IntegerField(primary_key=True)
    #id = models.AutoField(primary_key=True)
    name = models.CharField("Тема", max_length=200,
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
                           help_text="Пример: 1 день, 25 часов. Оставьте поле пустым, для одноразовой рассылки.", default="1 час", blank=True)
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

    def players_names(self):
        return " %s" % (", ".join([Topics.name for Topics in self.them.all()]))

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image_1))

    image_tag.short_description = 'Image'

    players_names.short_description = 'Темы'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Groups(models.Model):

    name = models.CharField("Название сообщества", max_length=200,
                            help_text="Введите название сообщества", blank=True, default="")

    token = models.TextField("Токен",
                             help_text="Введите токен сообщества", default="")

    id_group = models.BigIntegerField("ID сообщества",
                                      help_text="ID данного сообщества", blank=True, default=0)

    peer_id = models.BigIntegerField("ID беседы",
                                     help_text="ID привязанной беседы", blank=True, default=0)

    them = models.ForeignKey(Topics, verbose_name="Тема", on_delete=models.CASCADE)

    link = models.CharField("Ссылка", max_length=200,
                            help_text="Ссылка на сообщество", blank=True, default="")
    bol = models.BooleanField("Статус токена",
                              help_text="Статус работоспособности токена", blank=True,
                              default=False)
    bol_peer_id = models.BooleanField("Статус привязки",
                                      help_text="Статус привязки сообщества к беседе", blank=True,
                                      default=False)

    stat = models.BigIntegerField("Code",
                                  help_text="Error code", blank=True, default=0)

    peer_id_new = models.TextField("ID бесед",
                                   help_text="ID бесед", default="0")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сообщество"
        verbose_name_plural = "Сообщества"

    def save(self, *args, **kwargs):
        #self.name = "Не тест хе"
        #print(self.them_id)
        #super(Groups, self).save(*args, **kwargs)
        #print(self.stat, self.bol, kwargs)
        if self.stat == 0:
            t = Topics.objects.filter(id=self.them_id)
            #d = Groups.objects.filter(token=self.token)
            #print(t[0].soc)
            if self.id_group != 0:
                result = requests.post('http://127.0.0.1:5000',
                                       json={'token': self.token, 'soc': t[0].soc, "id": self.id_group})
            else:
                result = requests.post('http://127.0.0.1:5000',
                                       json={'token': self.token, 'soc': t[0].soc})
            #loop = asyncio.get_event_loop()
            #task = loop.create_task(fet_post(token=self.token, soc=t[0].soc))
            #loop.run_until_complete(asyncio.wait(task))
            #result = task.result()
            #print(result.text)
            res = result.json()
            status = res["status"]
            if status == 1:
                self.name = res["name"]
                self.id_group = res["id"]
                self.link = f"https://vk.com/club{res['id']}"
                self.bol = True
                #d[0].name = res["name"]
                #d[0].id_group = res["id"]
                #d[0].link = f"https://vk.com/club{res['id']}"
                #d[0].bol = True
                #d[0].save()
            else:
                self.name = "Не верный токен"
                #d[0].name = "Не верный токен"
                #d[0].save()
            super(Groups, self).save(*args, **kwargs)
        elif self.stat == 1:
            self.stat = 0
            super(Groups, self).save(*args, **kwargs)


class Users(models.Model):

    name = models.CharField("ФИО", max_length=200,
                            help_text="Введите фамилию имя отчество участника", blank=True, default="")

    link = models.CharField("Ссылка", max_length=500,
                            help_text="Введите ссылку на участника", blank=True, default="")
    rating = models.BigIntegerField("Рейтинг",
                                    help_text="Введите рейтинг участника", blank=True, default=0)

    user_id = models.CharField("ID", max_length=200,
                               help_text="ID пользователя в вк", blank=True, default="")

    date_editing = models.DateField(blank=False, verbose_name="Дата редактирования", default=datetime.date.today)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def save(self, *args, **kwargs):
        if self.user_id:
            person = Users.objects.filter(user_id=self.user_id)
            if person[0].link == self.link or person[0].name == self.name:
                super(Users, self).save(*args, **kwargs)
                return
        else:
            #super(Users, self).save(*args, **kwargs)
            #return
            t = Topics.objects.filter(soc="consultants")
            topics_id = t[0].id
            g = Groups.objects.filter(them_id=topics_id)
            token = g[0].token
            result = requests.post('http://127.0.0.1:5000',
                                   json={'token': token, 'user_link': self.link})

            res = result.json()
            if res["status"] == 1:
                self.user_id = res["user_id"]
                self.link = f"https://vk.com/id{res['user_id']}"
            super(Users, self).save(*args, **kwargs)
        #else:
            #super(Users, self).save(*args, **kwargs)
        #super(Users, self).save(*args, **kwargs)

class Questions(models.Model):

    question = models.TextField("Вопрос",
                                help_text="Введите вопрос", default="")

    bol = models.BooleanField("Статус отправки",
                              help_text="Статус отправки вопроса дня всем участникам", blank=True,
                              default=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def save(self, *args, **kwargs):
        t = Topics.objects.filter(soc="consultants")
        topics_id = t[0].id
        g = Groups.objects.filter(them_id=topics_id)
        token = g[0].token
        n = int(Questions.objects.latest('id').id) + 1
        result = requests.post('http://127.0.0.1:5000',
                               json={'token': token, 'question': self.question, 'question_id': n})

        res = result.json()
        if res["status"] == 1:
            self.bol = True
            super(Questions, self).save(*args, **kwargs)
        else:
            self.bol = False
            super(Questions, self).save(*args, **kwargs)




class Answers(models.Model):

    question = models.ForeignKey(Questions,
                                 verbose_name="Вопрос", on_delete=models.CASCADE)

    answer = models.TextField("Ответ",
                              help_text="Ответ участника", default="")

    user = models.ForeignKey(Users,
                             verbose_name="Участник", on_delete=models.CASCADE)

    date_editing = models.DateField(blank=False, verbose_name="Дата ответа", default=datetime.date.today)


    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"




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


