from django.shortcuts import render, redirect
from ..forms import MessageForm, Profile
from django.contrib import messages


def inbox(request):
    profile = request.user.profile
    messages_request = profile.received_messages.all()
    unread_messages_count = profile.received_messages.filter(is_read = False).count()
    context = {'messages_request': messages_request, 'unread_messages_count': unread_messages_count}
    return render(request, 'users/inbox.html', context)

def single_message(request, pk):
    profile = request.user.profile
    single_message = profile.received_messages.get(id = pk)
    if single_message.is_read == False:
        single_message.is_read = True
        single_message.save()
   
    context = {'single_message': single_message}
    return render(request, 'users/message.html', context )


def create_message(request, pk):
    recipient = Profile.objects.get(id = pk)
    
    try:
        sender = request.user.profile
    except:
        sender = None
    
    if request.method == 'POST':
        
        form = MessageForm(request.POST)
        if form.is_valid():
            
            try:
                message = form.save(commit=False)
                message.sender = sender
                message.recipient = recipient
                
                if sender:
                    message.name = sender.name
                    message.email = sender.email
                    
                message.save()
                messages.success(request, 'Your message has been submitted successfully!')
                return redirect('single-profile', pk = recipient.id )
                
            except Exception as e:
                print('Error al enviar el mensage:', e)
                messages.error(request, "Your message can't be submitted" )
        else:
            print("Errores del formulario", form.errors)
            
    else:
        
        form = MessageForm()
    context = {'form': form,
               'recipient': recipient}
    return render(request, 'users/message-form.html', context)