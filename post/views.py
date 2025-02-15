from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import Post, Comment
from.forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def post_index(request):
    post_list = Post.objects.filter(checked = False)
    url = request.get_full_path()
    if (url == '/post/kapali/'):
        post_list = Post.objects.filter(checked = True)

    

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
            ).distinct()

    paginator = Paginator(post_list, 5) # Show 25 contacts per page
    page = request.GET.get('sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    
    
    context = {
        'posts': posts,
    }
    return render(request, 'post/index.html', context)

def post_create(request):

    if request.user.is_authenticated == False:
        return redirect('postt:index')

    form = PostForm(request.POST or None, request.FILES or None )    
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Başarılı bir şekilde oluşturuldu.', extra_tags='mesaj-basarili-olusturma')
        return HttpResponseRedirect(post.get_absolute_url())     

    context = {
        'form': form
    }
    return render(request, 'post/form.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)  

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        if request.user.is_authenticated:
            form = CommentForm(isim=request.user.get_full_name, ornek='bu bir örnek alandır. modelde olmayan bir alan oluşturldu')

    comments = post.comments.all()
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }
    return render(request, 'post/detail.html', context)

def post_update(request, slug):

    post = get_object_or_404(Post, slug=slug)

    if request.user.is_authenticated == False:
        return redirect('postt:index')

    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellendi.', extra_tags='mesaj-basarili-guncelleme')  
        return HttpResponseRedirect(post.get_absolute_url())   
    

    context = {
        'form': form
    }
    return render(request, 'post/form.html', context)

def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)    
    post = get_object_or_404(Post, id = comment.post_id)

    if request.user.is_authenticated == False:
        return redirect('postt:index')
    form = CommentForm(request.POST or None, request.FILES or None, instance=comment, ornek='bu bir örnek alandır. modelde olmayan bir alan oluşturldu')
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellendi.', extra_tags='mesaj-basarili-guncelleme')  
        return HttpResponseRedirect(post.get_absolute_url())     

    context = {
        'form': form
    }
    return render(request, 'post/form.html', context)
    

def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user.is_authenticated == False:
        return redirect('postt:index')

    post.delete()
    return redirect('postt:index') 

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, id = comment.post_id)
    if request.user.is_authenticated == False:
        return redirect('postt:index')

    comment.delete()
    return HttpResponseRedirect(post.get_absolute_url()) 


