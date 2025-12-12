from django.shortcuts import render
def mathpage(request):
    return render(request, 'mathapp/math.html')

