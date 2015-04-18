# coding: utf-8
# ref: https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.ForeignKey.related_name

from django.core import validators
from django.db import models
from django.utils import six, timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import check_password


@python_2_unicode_compatible
class User(models.Model):
    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    password = models.CharField(_('password'), max_length=10, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    # config for auth.autheticate()
    USERNAME_FIELD = 'username'

    # add authBackend for authenticationSessionMiddleware checker
    backend = 'django.contrib.auth.backends.ModelBackend'

    def is_anonymous(self):
        return False

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        ordering = ('-id',)


@python_2_unicode_compatible
class Book(models.Model):
    label = models.CharField(_('label'), max_length=80, unique=True)
    users = models.ManyToManyField(User,
        verbose_name=_('users'), blank=True)

    author = models.ForeignKey(User, blank=True, related_name='publishs')

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'books'
        ordering = ('-id',)

# Usage
#   user.publishs.all()
#   user.book_set.all()
#   book.users.all()
