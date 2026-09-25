from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as banners
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import Message, Chat

User = get_user_model()

# Create your views here.
@login_required
def index(request):
    chats = Chat.objects.filter(Q(user_1 = request.user) | Q(user_2 = request.user)).order_by('-timestamp')
    

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

            chat = Chat.objects.filter(
                (Q(user_1=request.user) & Q(user_2=recipient)) |
                (Q(user_1=recipient) & Q(user_2=request.user))
            ).first()

            if not chat:
                chat = Chat.objects.create(user_1=request.user, user_2=recipient)
            
            Message.objects.create (
                chat = chat,
                sender=request.user,
                recipient=recipient,
                content=content
            )
            return redirect('messaging.chat', id = chat.id)
        except User.DoesNotExist:
            banners.error(request, f"User '{recipient_username}' does not exist.")
            return redirect('messaging.index')

@login_required
def send_message_in_chat(request, chat_id):
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id = chat_id)
        if chat.user_1.id == request.user.id:
            recipient = chat.user_2
        else:
            recipient = chat.user_1
        
        content = request.POST.get('content')
        Message.objects.create(
            chat = chat,
            sender = request.user,
            recipient = recipient,
            content = content
        )
        return redirect('messaging.chat', id = chat.id)

@login_required
def chat(request, id):
    chat_object = get_object_or_404(Chat.objects.filter(Q(user_1=request.user) | Q(user_2=request.user)),
                                    id=id
    )
    messages = Message.objects.filter(chat = chat_object).order_by('timestamp')
    recent_message = messages.last()
    if (recent_message): timestamp = recent_message.timestamp
    template_data = {}
    template_data['chat'] = chat_object
    template_data['messages'] = messages
    return render(request, 'messaging/chat.html', {'template_data': template_data})