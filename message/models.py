from django.contrib.auth.models import User
from django.db import models


class TimestampModel(models.Model):
    class Meta:
        abstract = True
    created = models.DateTimeField(auto_now_add=True)

class Message(TimestampModel):
    user = models.ForeignKey(User)
    status = models.TextField(null=False, max_length=140, blank=False)

    def __str__(self):
        return self.status

    @property
    def like_users(self):
        return [l.user for l in self.like_set.all() if l.like]

    @property
    def dislike_users(self):
        return [l.user for l in self.like_set.all() if not l.like]

class Like(TimestampModel):
    user = models.ForeignKey(User)
    message =models.ForeignKey(Message)
    like = models.BooleanField()

    def like_users(self):
        return [l.user for l in self.like_set.all() if l.like]

class Follow(TimestampModel):
    class Meta:
        unique_together = [("followed_user", "following_user"),]
    followed_user = models.ForeignKey(User, related_name='followed_by')
    following_user = models.ForeignKey(User, related_name='following')

    def __str__(self):
        return "User {0} follows user {1}".format(self.following_user.username, self.followed_user.username)