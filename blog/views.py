from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, ArtComment
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def blogHome(request): 
    filter=request.GET.get('filter')
    if filter:
        allPosts= Post.objects.filter(arttype=filter).all()
        is_home_page=True
        context={'allPosts': allPosts ,"is_home_page":is_home_page}
        return render(request, "blog/blogHome.html", context)
        
    allPosts= Post.objects.all()
    is_home_page=True
    context={'allPosts': allPosts ,"is_home_page":is_home_page}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    
    comments= ArtComment.objects.filter(post=post, parent=None)
    replies= ArtComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=ArtComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= ArtComment.objects.get(sno=parentSno)
            comment=ArtComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")    


def CreateNewPost(request):
    if request.method == "POST":
        image=request.POST.file('image')
        title=request.POST.get('title')
        tools=request.POST.get('tools')
        content=request.POST.get('content')
        arttype=request.POST.get('arttype')
        user=request.user
        print(title)
        print(content)
        print(image)
        messages.success(request, "Your post has been posted successfully")
        return redirect('/blogHome')
        
