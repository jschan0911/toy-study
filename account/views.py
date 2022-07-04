from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import auth
from account.models import myUser

def login(request):
    #POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd) 
        #받은 username과 password가 DB에 이미 있는건지 확인해보겠다는 의미
        #있는 계정이면 그 회원의 USER객체를 반환 없는계정이면 NONE 반환함
        if user is not None:
            auth.login(request,user)
            return redirect('first')
        else:
            return render(request, 'login.html')
    #GET 요청이 들어오면 login form을 담고있는 login.html을 띄어주는 역할을 해줌
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('first')

def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
        if request.method == 'POST':
            userid = request.POST['username']
            pwd = request.POST['password']
            pwd2 = request.POST['confirm']
            age = request.POST['age']
            # password와 confirm에 입력된 값이 같다면
            if pwd == pwd2:
                # user 객체를 새로 생성
                user = myUser.objects.create_user(username=userid, password=pwd, age = age)
                # 로그인 한다
                auth.login(request, user)
                return render(request, 'test.html')
            else:
                return render(request, 'again_signup.html')
            
    
        # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
        return render(request, 'signup.html')

def again_signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        pwd2 = request.POST['confirm']
        age = request.POST['age']

        # password와 confirm에 입력된 값이 같다면
        if pwd == pwd2:
            # user 객체를 새로 생성
            user = myUser.objects.create_user(username=userid, password=pwd, age=age)
            # 로그인 한다
            auth.login(request, user)
            return render(request, 'test.html')
        else:
            return render(request, 'again_signup.html')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'again_signup.html')

def test(request):
    point = 100
    user = get_object_or_404(myUser, pk = request.user.id)
    user.grade = ''
    user.save()
    if request.method == 'POST':
        if str(request.POST['plus']) == 'N':
            user = get_object_or_404(myUser, pk = request.user.id)
            user.grade += '덧셈 '
            user.save()
            point -= 25
        if str(request.POST['mult']) == 'N':
            user = get_object_or_404(myUser, pk = request.user.id)
            user.grade += '곱셈 '
            user.save()
            point -= 25
        if str(request.POST['minus']) == 'N':
            user = get_object_or_404(myUser, pk = request.user.id)
            user.grade += '뺄셈 '
            user.save()
            point -= 25
        if str(request.POST['div']) == 'N':
            user = get_object_or_404(myUser, pk = request.user.id)
            user.grade += '나눗셈 '
            user.save()
            point -= 25
        
        return render(request, 'result.html', {'grade':user.grade, 'point' : point})

    return render(request, 'test.html')

def plus_test(request):
    point = 100
    user = get_object_or_404(myUser, pk = request.user.id)

    if request.method == 'POST':
        if str(request.POST['plus']) == 'N':
            point -= 25
        if str(request.POST['mult']) == 'N':
            point -= 25
        if str(request.POST['minus']) == 'N':
            point -= 25
        if str(request.POST['div']) == 'N':
            point -= 25
        
        # 재시험 결과가 100점일 때 해당 유형 통과
        if point == 100:
            user.grade = user.grade.replace('덧셈', '')
            user.save()

        return render(request, 'result.html', {'grade':user.grade, 'point' : point})

    return render(request, 'plus_test.html')

def mult_test(request):
    point = 100
    user = get_object_or_404(myUser, pk = request.user.id)

    if request.method == 'POST':
        if str(request.POST['plus']) == 'N':
            point -= 25
        if str(request.POST['mult']) == 'N':
            point -= 25
        if str(request.POST['minus']) == 'N':
            point -= 25
        if str(request.POST['div']) == 'N':
            point -= 25
        
        if point == 100:
            user.grade = user.grade.replace('곱셈', '')
            user.save()

        return render(request, 'result.html', {'grade':user.grade, 'point' : point})

    return render(request, 'mult_test.html')

def minus_test(request):
    point = 100
    user = get_object_or_404(myUser, pk = request.user.id)

    if request.method == 'POST':
        if str(request.POST['plus']) == 'N':
            point -= 25
        if str(request.POST['mult']) == 'N':
            point -= 25
        if str(request.POST['minus']) == 'N':
            point -= 25
        if str(request.POST['div']) == 'N':
            point -= 25
        
        if point == 100:
            user.grade = user.grade.replace('뺄셈', '')
            user.save()

        return render(request, 'result.html', {'grade':user.grade, 'point' : point})

    return render(request, 'minus_test.html')

def div_test(request):
    point = 100
    user = get_object_or_404(myUser, pk = request.user.id)

    if request.method == 'POST':
        if str(request.POST['plus']) == 'N':
            point -= 25
        if str(request.POST['mult']) == 'N':
            point -= 25
        if str(request.POST['minus']) == 'N':
            point -= 25
        if str(request.POST['div']) == 'N':
            point -= 25
        
        if point == 100:
            user.grade = user.grade.replace('나눗셈', '')
            user.save()

        return render(request, 'result.html', {'grade':user.grade, 'point' : point})

    return render(request, 'div_test.html')