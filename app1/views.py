from django.shortcuts import render

def index(request):
    context = {
        'subtitle':'Eu vou aprender Django'
    }
    return render(request,'index.html',context)

    path('contato/', contato),
def contato(request):

    return render(request,'contato.html')