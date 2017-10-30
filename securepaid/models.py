# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
class SECUREPAY(models.Model):
    currency = models.CharField(max_length =500)
    amount = models.CharField(max_length=500)
    rmb_amount = models.CharField(max_length=500)
    vendor = models.CharField(max_length=500)
    reference = models.CharField(max_length=500)
    ipn_url = models.CharField(max_length=500)
    callback_url = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    note = models.CharField(max_length=500)
    terminal = models.CharField(max_length=500)
    timeout = models.CharField(max_length=500)

    def __str__(self):
        return self.reference+ ' : '+self.amount