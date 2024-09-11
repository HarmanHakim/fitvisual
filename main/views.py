from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306240080',
        'name': 'Harman Hakim',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)