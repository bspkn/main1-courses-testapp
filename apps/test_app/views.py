from django.shortcuts import render, redirect, HttpResponse
from .models import Blog, Comment ### this is for a blog...
from .models import User
# Create your views here.
def index(request):
    print("Running index method, calling out to User.")
    user = User.objects.login("speros@codingdojo.com","Speros")
    print (type(user))
    if 'error' in user:
        pass
    if 'theuser' in user:
        pass
    return HttpResponse("Done running userManager method. Check your terminal console.")

    # context = {
    # "blogs" : Blog.objects.all()
    # #select * from Blog
    # }
    # return render(request, 'test_app/index.html', context)

def blogs(request):
    #using ORM
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    #insert into Blog (title, blog, created_at, updated_at) values (title,blog, now(), now())
    return redirect('/')

def comments(request, id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog=blog)
    return redirect('/')
#
#
#   def index(request):

# DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
