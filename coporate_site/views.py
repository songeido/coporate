from django.shortcuts import render

def toppage(request):
    return render(request,'top.html')