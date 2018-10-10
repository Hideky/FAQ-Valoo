from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    username = models.CharField(max_length=40)
    question = models.CharField(max_length=255)
    answer = models.TextField(null=True)
    moderator = models.ForeignKey(User, related_name='answered', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'Ask by: {self.username} \nDate: {self.date} \nQuestion: {self.question} \nAnswer: {self.answer}'
