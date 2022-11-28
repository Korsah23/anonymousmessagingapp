from django.shortcuts import render
from .forms import MessageForm
from .models import Message
from django.http import HttpResponseRedirect
import uuid as id

# Create your views here.
def index(request):
    data = Message.objects.all()
    return render(request,"index.html",{"data":data})


def post(request):
    form = MessageForm(request.POST)
    #count = 0
    
    userid = str(id.uuid4())[:6]

    #check if form is valid
    if request.method == "POST":
        if form.is_valid():
            inputByUser = request.POST["userMessage"]
            userInput = Message.objects.create(userId=userid,userMessage=inputByUser)
            return HttpResponseRedirect("/")
    return render(request,"post.html",{"form":form})