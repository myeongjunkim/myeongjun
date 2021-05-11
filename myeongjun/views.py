from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'gallery.html')

def hometown(request):
    return render(request, 'hometown.html')

def myeongjun_main(request):
    return render(request, 'myeongjun_main.html')

def load_map(request):
    return render(request, 'load_map.html')

def cafe(request):
    return render(request, 'cafe.html')

def introduceme(request):
    return render(request, 'introduceme.html')