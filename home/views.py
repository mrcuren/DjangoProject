from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactFormMessage, ContactFormu,FAQ
from course.models import Category, Course,Comment
from django.template.base import VariableDoesNotExist
from programlama2 import settings

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    homecourses= Course.objects.all().order_by('-id')[:2]
    context = {'setting': setting, 'page': 'home', 'category': category,'homecourses': homecourses}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'hakkimizda', 'category': category}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'referanslarimiz', 'category': category}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir.Teşekkür ederiz")
            return HttpResponseRedirect('/iletisim')
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'iletisim.html', context)


def category_courses(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    courses = Course.objects.filter(category_id=id)
    context = {'courses': courses,
               'category': category,
               'categorydata': categorydata,
               }
    return render(request, 'courses.html', context)

def course_detail(request,id,slug):
    category = Category.objects.all()
    course = Course.objects.get(pk=id)
    comments=Comment.objects.filter(course_id=id,status='True')
    context = {'course': course,
               'category': category,
               'comments':comments,
               }
    return render(request, 'course_detail.html', context)



def faq(request):
    category = Category.objects.all()

    faq=FAQ.objects.all().order_by('ordernumber')
    context = {
               'category': category,
               'faq': faq,
               }
    return render(request, 'faq.html', context)
