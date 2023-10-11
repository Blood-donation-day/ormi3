from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    main_image = models.ImageField( blank=True, null=True) #upload_to='blog/',
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# blank=True는 '이 필드는 필수가 아니다'라는 내용입니다.
# null=True는 '이 필드는 새로 생성되어도 DB 비어있어도 된다.'