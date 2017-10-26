from django.db import models
from datetime import datetime


class Book(models.Model):
    title = models.CharField(max_length=30)
    year = models.DateField()
    description = models.CharField(max_length=1000)
    authors = models.ManyToManyField('Author')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='all_img', blank=True)
    prev = models.ImageField(upload_to='all_img', blank=True)
    # comment = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, default=0)
    # rating = models.OneToOneField('Rating', on_delete=models.CASCADE, blank=True, default=0)

    def __str__(self):
        return '{0}'.format(self.title)

class Rating(models.Model):
    like = models.IntegerField()
    dislike = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return '{0}'.format(self.title)


class Author(models.Model):
    name = models.CharField(max_length=30)
    date_bir = models.DateField()
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return '{0}'.format(self.name)
        # return '{0} {1}'.format(self.authors, self.category)



