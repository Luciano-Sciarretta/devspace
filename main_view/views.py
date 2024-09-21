from django.shortcuts import render


def main_view(request):
    return render(request, "main_view/main_view.html")