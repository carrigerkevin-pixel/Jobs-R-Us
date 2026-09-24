from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message, Chat

User = get_user_model()

# Create your views here.
@login_required
def index(request):
    chats = Chat.objects.filter(user_1 = request.user, user_2 = request.user).order_by('-timestamp')
    

    #messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    template_data = {}
    template_data['title'] = 'Messages'
    template_data['chats'] = chats
    return render(request, 'messaging/index.html', {'template_data': template_data})

@login_required
def send_message(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient_username', '').strip()
        content = request.POST.get('content', '').strip()

        #should I allow messages to self? 
        #if recipient_username == request.user_name:
            #messages.error('Cannot send messages to yourself.')
            #return redirect('messaging.index')

        try:
            recipient = User.objects.get(username=recipient_username)
            Message.objects.create (
                sender=request.user,
                recipient=recipient,
                content=content
            )
            return redirect('messaging.index')
        except User.DoesNotExist:
            messages.error('The recipient does not exist.')
            return redirect('messaging.index')

def chat(request, id):
    messages = Message.objects.filter(sender = request.user, recipient = request.user).order_by('-timestamp')
    if (messages[0] is not null): timestamp = messages[0].timestamp
    user_1 = User
    user_2 = Users.objects.filter(username = request.recipient_username)
    template_data = {}
    template_data['messages'] = messages
    return render(request, 'messaging/chat.html', {'template_data': template_data})