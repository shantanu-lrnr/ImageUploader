from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm

# Create your views here.

def home(request):
    images = Image.objects.all()
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request,'myapp/home.html',{'form':form,'images':images})
