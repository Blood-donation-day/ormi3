from django.db import models
from users.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='posts/images/%y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str__(self):
        return f'{self.author} - {self.pk}'
    
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} - {self.post} - {self.pk}'
    
    
class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    # def Meta(self):
    #     unique