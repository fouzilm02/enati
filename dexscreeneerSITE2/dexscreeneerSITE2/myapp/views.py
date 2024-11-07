from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from pymongo.errors import DuplicateKeyError
import re
import uuid

db = settings.MONGO_DB
users_collection = settings.MONGO_DB['users']

def home(request):
    return render(request, 'auth/home.html')

class CustomUser:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.is_authenticated = True
