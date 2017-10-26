# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import pytz
import datetime

@python_2_unicode_compatible
class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})




class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    name = models.CharField(max_length=256)
    birthday = models.DateTimeField(null=True, blank=True)
    birthday_utc = models.DateTimeField(null=True, blank=True, editable=False)
    hometown = models.ForeignKey("cities.City", verbose_name=_("hometown"), null=True, blank=True)

    def get_absolute_url(self):
        return reverse('userprofile-view', args=[self.pk])



    @classmethod
    def create(cls, request=None, **kwargs):
        profile = cls(**kwargs)
        profile.name = profile.user.name
        profile.save()
        return profile

    def localize_birthday(self):
        if self.hometown is not None:
            self.birthday_utc = self.hometown.timezone.localize(self.birthday.replace(tzinfo=None))

    def profile_image_url(self, size=40):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
        if len(fb_uid):
            return "http://graph.facebook.com/{uid}/picture?width={size}&height={size}".format(uid=fb_uid[0].uid, size=size)

        return "http://www.gravatar.com/avatar/{md5}?s={size}".format(md5=hashlib.md5(self.user.email.encode('utf-8')).hexdigest(), size=size)


    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
        self.user.name = self.name
        self.user.save()
        self.localize_birthday()
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save(sender, **kwargs):
    user, created = kwargs["instance"], kwargs["created"]
    if created:
        UserProfile.create(user=user)
