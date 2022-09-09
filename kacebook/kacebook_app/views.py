from django.shortcuts import render
from kacebook_app.models import Message
from kacebook_app.forms import MessageForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    """the home page for learning log"""
    messages = Message.objects.all()
    users = User.objects.all()
    context = {"messages":messages, "users":users}
    return render(request, 'kacebook_app\index.html', context)

def friends(request):
    users = User.objects.all()
    context = {"users":users}
    return render(request, 'kacebook_app/friends.html', context)

def new_message(request):
    """write a new message"""
    users = User.objects.all()
    messages = Message.objects.all()
    if request.method != 'POST':
        # no data submitted, create a blank forum
        form = MessageForm()
    else:
        # POST data submitted, process data
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.owner = request.user
            new_message.save()
            return HttpResponseRedirect(reverse('kacebook_app:index'))

    context = {'form':form, 'users':users}
    return render(request, 'kacebook_app/new_message.html', context)

def profile(request, user_id):
    """show your chat with a single user"""
    user = User.objects.get(id=user_id)
    messages = Message.objects.all()
    if request.method != 'POST':
        form = MessageForm()
    else:
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.owner = request.user
            new_message.reciever = user
            new_message.save()
            form = MessageForm()
            #return HttpResponseRedirect(reverse('kacebook_app:friends'))
    context = {'u':user, 'form':form, 'messages':messages}
    return render(request, 'kacebook_app/profile.html', context)
