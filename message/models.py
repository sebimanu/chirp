from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimestampModel(models.Model):
    class Meta:
        abstract=True
    created = models.DateTimeField(auto_now_add=True)


class Message(TimestampModel):
    user=models.ForeignKey(User)
    status=models.TextField(null=False, max_length=140, blank=False)



class Like(TimestampModel):
    user=models.ForeignKey(User)
    message=models.ForeignKey(Message)
    like=models.BooleanField()



class Follow(TimestampModel):
    followed_user=models.ForeignKey(User, related_name='follwed_by')
    following_user=models.ForeignKey(User, related_name='following')