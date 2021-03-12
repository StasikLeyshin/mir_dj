from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.utils.safestring import mark_safe

from .models import Topics, Rassilka, Groups, Users, Questions, Answers
from article.forms import ItemChangeListForm
from django.utils.html import format_html

# Register your models here.

admin.site.register(Topics)
#admin.site.register(Photo)

#class NoteAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('title',)} # new


'''@admin.register(Rassilka)
class Rassilkaadmin(admin.ModelAdmin):

    list_display = ("name", "them", "date_start", "period")
    list_filter = ("them")'''


#admin.site.register(Rassilka)

'''class ItemChangeList(ChangeList):

    def __init__(self, request, model, list_display,
        list_display_links, list_filter, date_hierarchy,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin, sortable_by):

        super(ItemChangeList, self).__init__(request, model, list_display,
        list_display_links, list_filter, date_hierarchy,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin, sortable_by)

        # these need to be defined here, and not in ItemAdmin
        self.list_display = ['name', 'date_start', 'them']
        self.list_display_links = ['name']
        #self.list_editable = ['them']


class RassilkaAdmin(admin.ModelAdmin):

    def get_changelist(self, request, **kwargs):
        return ItemChangeList

    def get_changelist_form(self, request, **kwargs):
        return ItemChangeListForm


admin.site.register(Rassilka, RassilkaAdmin)'''

@admin.register(Rassilka)
class RassilkaAdmin(admin.ModelAdmin):
    list_display = ('name', 'period', 'date_start', 'players_names')
    list_filter = ('name', 'period', 'date_start')
    search_fields = ('name', 'period', 'date_start')
    save_on_top = True
    save_as = True
    #readonly_fields = ('get_image',)
    #fields = ((f'image_{i+1}' for i in range(10)),)
    '''fields = (('name'),
              ('text'),
              ('post'),
              ('date_start', 'period'),
              ('them'),
              ('image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8', 'image_9', 'image_10')
              )'''
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Настройка сообщения', {
            'fields': (('text', 'post'),)
        }),
        ('Работа со временем', {
            'fields': (('date_start', 'period'),)
        }),
        ('Темы', {
            'fields': ('them',)
        }),
        ('Изображения', {
            'classes': ('collapse',),
            'fields': (('image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8', 'image_9', 'image_10',),)
        }),
    )
    '''def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image_1.url}'/>")#width='50' height='60'")
        #return mark_safe("<img src='https://dvmn.org/filer/canonical/1591892373/669/'>")
        #return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.images_1.url))

    get_image.short_description = 'Изображение' '''
    #fields = ['them']

@admin.register(Groups)
class Groups(admin.ModelAdmin):
    list_display = ('name', 'id_group', 'them', 'show_firm_url', 'bol', 'bol_peer_id')
    list_filter = ('bol', 'bol_peer_id', 'them__name', 'name')
    search_fields = ('name', 'id_group', 'link', 'them__name')
    list_display_links = ('name', 'id_group')
    readonly_fields = ('name', 'id_group', 'peer_id', 'link', 'bol', 'bol_peer_id', 'show_firm_url', 'peer_id_new')
    save_on_top = True
    save_as = True

    fieldsets = (
        ("Название", {
            'fields': ('name',)
        }),
        ('Данные сообщества', {
            'fields': ('token', 'them', 'show_firm_url',)
        }),
        ('ID', {
            'fields': ('id_group', 'peer_id', 'peer_id_new')
        }),
        ('Статусы', {
            'fields': ('bol', 'bol_peer_id',)
        }),
    )



    def show_firm_url(self, obj):
        return format_html("<a href='{url}' target='_blank' >{url}</a>", url=obj.link)

    show_firm_url.short_description = "Ссылка"

@admin.register(Users)
class Users(admin.ModelAdmin):
    list_display = ('name', 'show_firm_url', 'rating')
    list_filter = ('name', 'link', 'rating')
    search_fields = ('name', 'link', 'rating')
    list_display_links = ('name',)
    readonly_fields = ('date_editing', 'user_id')
    list_editable = ('rating',)
    save_on_top = True
    save_as = True
    fieldsets = (
        ("Участник", {
            'fields': ('name', 'link', 'rating', 'user_id')
        }),
        ('Дата реадктирования', {
            'fields': ('date_editing',)
        }),
    )

    def show_firm_url(self, obj):
        return format_html("<a href='{url}' target='_blank' >{url}</a>", url=obj.link)

    show_firm_url.short_description = "Ссылка"

@admin.register(Answers)
class Answers(admin.ModelAdmin):
    list_display = ('question', 'user', 'date_editing')
    list_filter = ('question__question', 'user__name')
    search_fields = ('question__question', 'user__name', 'date_editing')
    list_display_links = ('question',)
    readonly_fields = ('date_editing',)
    save_on_top = True
    save_as = True


@admin.register(Questions)
class Questions(admin.ModelAdmin):
    list_display = ('question', 'bol')
    list_filter = ('question', 'bol')
    search_fields = ('question',)
    list_display_links = ('question',)
    readonly_fields = ('bol',)
    save_on_top = True
    save_as = True
#admin.site.register(Questions)
