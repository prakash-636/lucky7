from django.shortcuts import render


import random

# Create your views here.

def index(request):

    numbers = (1,2,3,4,5,6)
    d1 = random.choice(numbers)
    d2 = random.choice(numbers)
    dice2 = d1+d2
    print(F"hi number is {dice2}")
    return render(request,"index.html",{'dicevalue':dice2,'Dicev1':d1,'Dicev2':d2})
    



