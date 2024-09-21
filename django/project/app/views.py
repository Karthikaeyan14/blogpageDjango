from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404
from .forms import ContactForm

#static demo data 
'''posts=[
        {'id':1,'title':'post1','content':'Content of Post 1'},
        {'id':2,'title':'post2','content':'Content of Post 2'},
        {'id':3,'title':'post3','content':'Content of Post 3'},
        {'id':4,'title':'post4','content':'Content of Post 4'},

    ]'''
def home(request):
    blog_title='Latest Posts'
    #getting data from post model
    posts=Post.objects.all()
    return render(request,'index.html',{'title':blog_title,'posts':posts})

def value(request,post_id):
    #static data
    #post=next((item for item in posts if item['id']==int(post_id)),None)
    #This is logging method
    #logger=logging.getLogger("TESTING")
    #logger.debug(f'post variable is {post}')
    try:
        post=Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("post does not exist!")
    
    
    return render(request,'details.html',{'post':post})

def old_url(request):
    return redirect(reverse('app:new_url'))

def new_url(request):
    return HttpResponse("THis is the new url")


def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        logger=logging.getLogger("TESTING")
        if form.is_valid():
           logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message'] }')
           success_message='Your Email has been sent'
           return render(request,"contact.html",{'form':form ,'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request,"contact.html",{'form':form ,'name':name,'email':email,'message':message})
    return render(request,"contact.html")


def about(request):
    return render(request,'about.html')