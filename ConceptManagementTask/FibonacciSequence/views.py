from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fun(request):

    return render(request, "fbb.html")


def result(request):
    from datetime import datetime
    start = datetime.now()
    n = int(request.POST["num"])
    y = 0
    l1 = [1,1]
    for x in range(n):
        if n == 1 or n == 2:
            break
        else:
            y = l1[x] + l1[x + 1]
            l1.append(y)

    end = datetime.now()
    time_taken = end - start
    # print('Time: ', time_taken)
    return render(request, "result.html", {"result":l1[n-1], "Nth": n, "time": time_taken})
