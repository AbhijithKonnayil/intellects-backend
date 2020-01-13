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
    upvotes = models.ForeignKey(User, on_delete=models.CASCADE,related_name='upvotes')
    downvotes = models.ForeignKey(User, on_delete=models.CASCADE,related_name='downvotes')
    post_type = models.CharField(max_length=50, choices=POST_TYPE_CHOICES)
    is_answer = models.NullBooleanField(null=True, default=None)

    def __str__(self):
        return '{}'.format(self.text)


class Comment (models.Model):
    text = models.CharField(max_length=1000, null=False, blank=False)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.text)

