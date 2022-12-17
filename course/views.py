from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from course.models import CommentForm, Comment
# Create your views here.
def index(request):
    return HttpResponse("Course Page")

@login_required(login_url='/login')
def addcomment(request,id):

    url = request.META.get('HTTP_REFERER')  # get last url
    #return HttpResponse(url)
    if request.method == 'POST':
        # check post
        form = CommentForm(request.POST)

        if form.is_valid():
            current_user = request.user
            data = Comment()  # create relation with model
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.course_id=id
            data.user_id=current_user.id
            data.save()  # save data to table
            messages.success(request, "Yorumunuz gönderildi. İlginiz için teşekkür ederiz.")
            return HttpResponseRedirect(url)

    messages.warning(request, "Yorumunuz kaydedilmedi. Lütfen kontrol ediniz.")
    return HttpResponseRedirect(url)
