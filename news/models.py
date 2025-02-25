from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from user.models import CustomUser




class Category(models.Model):
    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class News(models.Model):
    name = models.CharField(max_length=100, verbose_name='News Name')
    title = models.CharField(max_length=100, verbose_name='News Title')
    text = models.TextField(verbose_name='News Text')
    rasm = models.ImageField(upload_to='rasmlar/', null=True, blank=True, verbose_name='Image')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_news', verbose_name='Author')
    tur = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='Slug')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    views = models.PositiveBigIntegerField(default=0, verbose_name='Views')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created']




class Comment(models.Model):
    izoh = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    news = models.ForeignKey(News, on_delete= models.CASCADE,related_name='comments', null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.izoh[:50]
