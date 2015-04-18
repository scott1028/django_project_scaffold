# coding: utf-8

print 'start to patching django!'

# fix django 1.8 support tastypie
from django.db import transaction
transaction.commit_on_success = transaction.atomic
