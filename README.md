# How to Start

1. django-admin.py startproject webService
2. mkdir -p modules/daoService && touch modules/__init__.py && python manage.py startapp daoService
3. add daoService models.py

        from django.core import validators
        from django.db import models
        from django.utils import six, timezone
        from django.utils.translation import ugettext_lazy as _

        # Create your models here.
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
            first_name = models.CharField(_('first name'), max_length=30, blank=True)
            last_name = models.CharField(_('last name'), max_length=30, blank=True)
            email = models.EmailField(_('email address'), blank=True)
            is_staff = models.BooleanField(_('staff status'), default=False,
                help_text=_('Designates whether the user can log into this admin '
                            'site.'))
            is_active = models.BooleanField(_('active'), default=True,
                help_text=_('Designates whether this user should be treated as '
                            'active. Unselect this instead of deleting accounts.'))
            date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
            class Meta:
                db_table = 'users'
                ordering = ('-id',)

4. update settings.py

        INSTALLED_APPS = (
            # 關閉所有內建 App Modules
            # 'django.contrib.admin',
            # 'django.contrib.auth',
            # 'django.contrib.contenttypes',
            # 'django.contrib.sessions',
            # 'django.contrib.messages',
            # 'django.contrib.staticfiles',
            'modules.daoService',
        )

        MIDDLEWARE_CLASSES = (
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            # disable csrf-token feature
            # 'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        )

4. python manage.py makemigrations
        ( generator create table sql statement )

5. python manage.py migrate

* if Model Change, you must python manage.py makemigrations and python manage.py migrate.
* Tastypie reousrces.py 下的 @transaction.commit_on_success 要改為 transaction.atomic, 因為 Django 1.8 沒有這個 Method.
