from django.db import models
from user_manager.models import User

class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200,null=False,blank=False)
    content = models.CharField(max_length=4000,null=False,blank=False)
     
    def __str__(self):
         return "{}".format(self.title)

class Comment(models.Model):
    text = models.CharField(max_length=500,null=False,blank=False)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_comments")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.text)
         
