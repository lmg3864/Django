from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, "calculators/calculation.html")

def result(request):
    first_num = int(request.GET.get('first_num'))
    second_num = int(request.GET.get('second_num'))
    
    if second_num != 0:
        div = first_num/second_num
    else:
        div = "error"
    
    context = {
        "first_num" : first_num,
        "second_num" : second_num,
        "sub" : first_num - second_num,
        "mul" : first_num * second_num,
        "div" : div
    }

    return render(request, "calculators/result.html", context)