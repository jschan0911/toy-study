from django.db import models

# #Blog객체 만들기
# class Problem(models.Model): #models안의Model을 상속해야함
#     title = models.CharField(max_length=200)  #뒤에 어떤타입인지도 명시
#     body = models.TextField()
#     # # photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
#     # date = models.DateTimeField(auto_now_add=True) #자동으로 지금시간 추가하겠다는 말
#     # # writer = models.ForeignKey(User,on_delete=models.CASCADE)
#     # # writer = models.ForeignKey(myUser, on_delete=models.CASCADE)
#     # # writer = models.CharField(myUser, on_delete=models.CASCADE)
#     # writer = models.ForeignKey(myUser, null= True, on_delete = models.CASCADE)  #
#     # # writer = models.ForeignKey(myUser, on_delete = models.CASCADE)

#     def __str__(self): ##str 소문자로 해줘야함
#         return self.title 

# Create your models here.
