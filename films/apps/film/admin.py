from django.contrib import admin
from django.utils.safestring import mark_safe
from embed_video.admin import AdminVideoMixin

from .models import *

class FilmAdmin(AdminVideoMixin, admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ("name", 'view', 'genre', 'get_img')
    readonly_fields = ('get_img', 'get_video')
    list_display_links = ("name", 'view', 'get_img')
    ordering = ['-view']
    def get_video(self, obj):
        return mark_safe(f'<video src={obj.path_video.url} autoplay muted controls ')

    def get_img(self, obj):
        return mark_safe(f'<img alt="sorry" src={obj.img.url} width="50" height="60"')

    get_img.short_description = 'Current image'
    get_video.short_description = 'Current video'

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'another_films', 'get_img')
    list_display_links = ('name', 'another_films', 'get_img')
    readonly_fields = ['get_img']

    def get_img(self, obj):
        return mark_safe(f'<img alt="sorry" src={obj.img.url} width="50" height="60"')

    get_img.short_description = 'Film image'

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_text', 'film')
    
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'reviews')

class FilmShotsAdmin(admin.ModelAdmin):
    list_display = ['get_img']
    readonly_fields = ['get_img']

    def get_img(self, obj):
        return mark_safe(f'<img alt="sorry" src={obj.img.url} width="50" height="60"')

class UserPhotoAdmin(admin.ModelAdmin):
    list_display = ['get_photo']
    readonly_fields = ['get_photo']
    def get_photo(self, obj):
        return mark_safe(f'<img alt="sorry" src={obj.photo.url} width="50" height="60"')

    get_photo.short_description = 'Current image'

class LikedFilmsAdmin(admin.ModelAdmin):
    list_display = ('user', 'films')

class UserCreatedFilmsAdmin(admin.ModelAdmin):
    list_display = ('user', 'films')

class UserDescriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'description')

admin.site.register(Film, FilmAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre)
admin.site.register(UserCreatedFilms, UserCreatedFilmsAdmin)
admin.site.register(LikedFilms, LikedFilmsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(FilmShots, FilmShotsAdmin)
admin.site.register(UserPhoto, UserPhotoAdmin)
admin.site.register(UserDescription, UserDescriptionAdmin)