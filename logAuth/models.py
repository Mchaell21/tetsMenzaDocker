from django.db import models

class ImageServ(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='assets/serviceImages')
    is_enabled = models.BooleanField(default=True)

    def show_image(self):
        if self.is_enabled:
            return self.image.url
        else:
            return None

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='assets/promoImages')

    def __str__(self):
        return self.post.title
    
class LogoImg(models.Model):
    titleLogo = models.CharField(null=True, blank=True, max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='assets/logoImage')
    is_enabled = models.BooleanField(default=True)

    def show_image(self):
        if self.is_enabled:
            return self.image.url
        else:
            return None
