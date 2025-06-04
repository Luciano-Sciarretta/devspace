from django.shortcuts import render


def inbox(request):
    profile = request.user.profile
    messages_request = profile.received_messages.all()
    unread_messages_count = profile.received_messages.all().count()
    context = {'messages_request': messages_request, 'unread_messages_count': unread_messages_count}
    return render(request, 'users/inbox.html', context)