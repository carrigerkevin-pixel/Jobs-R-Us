from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

# Create your views here.
@login_required
def index(request):
    messages = Message.objects.filter(recipient=request.user)
    template_data = {}
    template_data['title'] = 'Messages'
    template_data['messages'] = messages
    return render(request, 'messages/index.html', {'template_data': template_data})

@login_required
def message(request):
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

