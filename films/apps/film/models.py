from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User


class Genre(models.Model):
    genre = models.CharField('Genre', max_length = 200)

    def __str__(self):
        return self.genre
class Film(models.Model):
    name = models.CharField('Film name', max_length = 150)
    producer = models.CharField('Produser', max_length = 100)
    ceated_at = models.DateField('Created date', auto_now_add = True)
    rating = models.IntegerField('Rating', default = 0)
    warning_age = models.IntegerField('Warning age', default = 0)
    description = models.TextField('Description')
    img = models.ImageField('Image', upload_to = 'media', blank = True)
    view = models.IntegerField('Views', default = 0)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    video = EmbedVideoField('embed video', null = True, blank =  True)
    path_video = models.FileField('path video', upload_to = 'video', null = True, blank =  True)

    def __str__(self):
        return self.name
class Actor(models.Model):
    name = models.CharField('Actor name', max_length = 200)
    another_films = models.TextField('Actor another films')
    age = models.IntegerField('Age', default = 0)
    img = models.ImageField('Image', upload_to = 'media', null = True)
    description = models.TextField('Actor description', null = True)
    film = models.ForeignKey(Film, on_delete = models.CASCADE, null = True, blank = True)

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'

    def __str__(self):
        return self.name
class Review(models.Model):
    review_author = models.CharField('Review author', max_length = 100)
    review_text = models.TextField('Text')
    film = models.ForeignKey(Film, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.review_text
class Answer(models.Model):
    answer_author = models.CharField('Answer author', max_length = 100)
    answer_text = models.TextField('Text')
    reviews = models.ForeignKey(Review, on_delete = models.CASCADE)

    def __str__(self):
        return self.answer_text
class FilmShots(models.Model):
    img = models.ImageField('Image', upload_to = 'media', blank = True)
    film = models.ForeignKey(Film, on_delete = models.CASCADE, null = True, blank = True)

    class Meta:
        verbose_name = 'Filmshot'
        verbose_name_plural = 'Filmshots'
class UserPhoto(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to = 'media', null = True, blank = True)

    class Meta:
        verbose_name = 'UserPhoto'
        verbose_name_plural = 'UserPhotos'
class LikedFilms(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    films = models.ForeignKey(Film, on_delete = models.CASCADE, null = True)


    def __str__(self):
        return f'user: {self.user.username}, film: {self.films.name}'
    class Meta:
        verbose_name = 'Likedfilm'
        verbose_name_plural = 'Likedfilms'
class UserCreatedFilms(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    films = models.ForeignKey(Film, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return f'user: {self.user.username}, film: {self.films.name}'
    class Meta:
        verbose_name = 'Usercreatedfilm'
        verbose_name_plural = 'Usercreatedfilms'

class UserDescription(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    description = models.TextField('description')

    def __str__(self):
        return f'user: {self.user}, description: {self.description}' 
    
    class Meta:
        verbose_name = 'Userdescription'
        verbose_name_plural = 'Userdescriptions'
