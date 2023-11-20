from django.shortcuts import render

# Create your views here.
def rishi(request):
    data=11
    d={'a':data}
    return render(request,'if_cond.html',context=d)


def loki(request):
    d={'a':10,'b':21}
    return render(request,'if_else.html',context=d)

def shaju(request):
    d={'a':10,'b':12,'c':11}
    return render(request,'if_elif.html',context=d)

def Praveen(request):
    d={'a':10,'b':12,'c':9}
    return render(request,'nested_if.html',d)
