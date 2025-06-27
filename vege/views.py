from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def receipes(request):
    if request.method == "POST":
       data= request.POST
       receipe_image=request.FILES.get('receipe_image')
       receipe_name= data.get('receipe_name')
       receipe_description= data.get('receipe_description')

     
       Receipe.objects.create(
           receipe_image=receipe_image,
           receipe_name=receipe_name,
           receipe_description=receipe_description,

           
       )
   
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset= queryset.filter(receipe_name__icontains = request.GET.get ('search'))


    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        # If the user uploads a new image, replace the old one
        if request.FILES.get('receipe_image'):
            receipe_image = request.FILES.get('receipe_image')
            queryset.receipe_image = receipe_image

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        queryset.save()
        return redirect('/receipes/')

    context = {'receipe': queryset}
    return render(request, 'update_receipes.html', context)


def delete_receipe(request,id):
    receipe = Receipe.objects.get(id=id)
    receipe.delete()
    return redirect('/receipes/')

    
    

