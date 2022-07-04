from django.shortcuts import get_object_or_404, render

from account.models import myUser

def first(request):
    plus = 0
    mult = 0
    minus = 0
    div = 0

    # If user is logged in
    if request.user.id != None:
        user = get_object_or_404(myUser, pk = request.user.id)
        if str(user.grade).find('덧셈') != -1:
            plus = 1
        if str(user.grade).find('곱셈') != -1:
            mult = 1
        if str(user.grade).find('뺄셈') != -1:
            minus = 1
        if str(user.grade).find('나눗셈') != -1:
            div = 1

        return render(request, 'first.html', {"plus" : plus, "mult" : mult, "minus" : minus, "div" : div})

    
    return render(request, 'first.html', {"plus" : plus, "mult" : mult, "minus" : minus, "div" : div})
# Create your views here.
