from django.db import models
from user.models import CustomUser
from news.models import News


class Like(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='likes', verbose_name='Bosilgan layk')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Yaratilgan vaqt')

    def __str__(self):
        return f"Like by {self.user.username} on {self.news.title}"

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = ('news', 'author')  # Bir foydalanuvchi bir yangilikni bir marta "yoqtirishi" mumkin



class Rating(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='ratings')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 dan 5 gacha baholash
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.value} by {self.user.username} on {self.news.title}"

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ('news', 'author')  # Bir foydalanuvchi bir yangilikni bir marta baholashi mumkin