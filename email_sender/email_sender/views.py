from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail



def index(request):
    subject = "i am subject"
    message = "i am message"
    email_from = "artidhakulkar31@gmail.com"
    email_to = ["artidhakulkar31@gmail.com", "artidhakulkar3112@gmail.com"]
    send_mail(subject, message, email_from, email_to)
    return render(request, "index.html")
