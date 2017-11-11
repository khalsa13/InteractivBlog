from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from urllib.parse import quote_plus
from .forms import PostForm
# Create your views here.
from .models import Post


def post_home(request):
    query_set_list=Post.objects.all()
    requestReceive = request.GET.get("q")
    if requestReceive:
        query_set_list = query_set_list.filter(title__icontains=requestReceive)

    paginator = Paginator(query_set_list, 3)  # Show 25 contacts per page


    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_set = paginator.page(paginator.num_pages)

    context={
        "title":"Hey!! Welcome",
        "query_set":query_set,

    }
    return render(request,"home.html",context)


def create(request):
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Succesfully Created New Post :)")

    context={
        "form":form,
    }
    return render(request,"form_add.html",context)


def cover(request):

    context = {
    }

    return render(request, "Front.html", context)


def delete(request,id=None):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"SuccesFully Deleted The Post")
    return HttpResponseRedirect('/posts')


def details(request,slug=None):
    instance=get_object_or_404(Post,slug=slug)
    share_url = quote_plus(instance.content)
    context = {
        "title": "Hey!! Welcome",
        "instance": instance,
        "share_url":share_url
    }
    return render(request, "details.html", context)




def update(request,slug=None):
    instance=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Succesfully Updated Post :)")
        return HttpResponseRedirect('/posts/')
    context = {
        "instance": instance,
        "form":form,
    }
    return render(request, "form_add.html", context)
