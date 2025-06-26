from django.shortcuts import render

from django.http import HttpResponse


def about_page(request):
    
    return HttpResponse("<h1>Hey I am a about page!</h1>")

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey I am a success page!</h1>")

def home(request):

    peoples = [
        {'name': 'Nikita Maan','age' : 21},
        {'name': 'Nitin Maan','age' : 26},
        {'name': 'Rozi Chilwal','age' : 22},
        {'name': 'Anisha Lamba','age' : 31},
        {'name': 'Siya Chahar','age' : 15}
    ]

    vegetables = ['Pumpkin','Tomato','Potato']

    
    for people in peoples:
        print(people)

    for person in peoples:
        person['can_vote'] = person['age'] >= 18    
    return render(request, 'home/index.html', context = {'page':'Django 2024 Tutorial','peoples': peoples,'vegetables':vegetables})

def about(request):
    context= {'page':'about'}
    return render(request, 'home/about.html',context)


def contact(request):
    context= {'page':'contact'}
    return render(request, 'home/contact.html',context)


