from django.shortcuts import render
from .models import Image
# Create your views here.
def index(request):
    if request.method=="POST":
        image = request.FILES.get("image")
        caption = request.POST.get("caption")
        img = Image(image=image,caption=caption)
        img.save()
    
    images = Image.objects.all()
    return render(request,"a/index.html",{"images":images})

def elaborate(request,id):
    img = Image.objects.get(id=id)
    return render(request,"a/elaborate.html",{"img":img})