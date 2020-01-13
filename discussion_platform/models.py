from django.db import models
from user_manager.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class Tag(models.Model):
    title = models.CharField(max_length=20)
    count = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return '{}'.format(self.title)

class Post(models.Model):
    POST_TYPE_CHOICES = (('q', 'Question'), ('a', 'Answer'))

    def AnswerValidator(value, self):
        if not self.post_type == 'a' and self.is_answer:
            raise ValidationError(
                ('Question cannot be accepted as anwser'),)

    text = models.CharField(max_length=1000, null=False, blank=False)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    upvotes = models.ManyToManyField(User,related_name='upvotes')
    downvotes = models.ManyToManyField(User,related_name='downvotes')
    post_type = models.CharField(max_length=50, choices=POST_TYPE_CHOICES)
    question = models.ForeignKey('discussion_platform.Post',on_delete=models.CASCADE,null=True,blank=True,related_name='questions')
    answer = models.OneToOneField('discussion_platform.Post',on_delete=models.CASCADE,null=True,blank=True,related_name='answer_of')

    def __str__(self):
        return '{}'.format(self.text)


class Comment (models.Model):
    text = models.CharField(max_length=1000, null=False, blank=False)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.text)

