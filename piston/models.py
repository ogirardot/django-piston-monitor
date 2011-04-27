#!/usr/bin/python
# -*- coding: utf-8 -*-
import django.dispatch
from django.db import models

class Call(models.Model):
	url = models.CharField(max_length=500)                         
	method = models.CharField(max_length=6)
	timestamp = models.DateTimeField(auto_now=True)
	caller = models.TextField() 
	parameters = models.TextField(null=True)

# define signals to be emitted when API called
api_called = django.dispatch.Signal(providing_args=["url", "method", "caller", "parameters"])
