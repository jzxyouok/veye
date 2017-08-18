#!/usr/bin/env python
# encoding: utf-8

"""
@version: 0.1
@author: stskyblade
@contact: stskyblade@outlook.com
@file: urls.py
@time: 17-8-17 上午9:43
"""

from django.conf.urls import url
from . import views


app_name = "user"
urlpatterns = [
    url(r"^$", views.hello, name="hello"),
    url(r"^register_form$", views.register_form, name="register_form"),
    url(r"^register$", views.register, name="register"),
    url(r"^login_form$", views.login_form, name="login_form"),
    url(r"^login$", views.login, name="login"),
    url(r"^logout$", views.logout, name="logout"),
]