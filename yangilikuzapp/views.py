from django.shortcuts import render,get_object_or_404
from .models import News,Category
from .forms import contactform,userregistrationform
from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

   

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        news = News.objects.filter(title__contains=searched)
        return render(request, 'news/pages/search_venues.html', {'searched':searched, 'news':news})
    else:
        return render(request, 'news/pages/search_venues.html', {})

def IndexView(request):
    yangilik = News.objects.all().order_by('-publish_time')[:5]
    yangilik2 = News.objects.all().order_by('-publish_time')[5:9]
    yangilik3 = News.objects.all().order_by('-publish_time')[:4]
    categories=Category.objects.all()
    uz = News.objects.filter(category_id=5)
    jahon = News.objects.filter(category_id=6)
    iqtisodiyot = News.objects.filter(category_id=7)
    jamiyat = News.objects.filter(category_id=8)
    fan = News.objects.filter(category_id=9)
    sport = News.objects.filter(category_id=10)
    context = {
        'yangilik': yangilik,
        'yangilik2' : yangilik2,
        'yangilik3': yangilik3,
        'category': categories,
        'uz': uz,
        'jahon': jahon,
        'iqtisodiyot': iqtisodiyot,
        'jamiyat': jamiyat,
        'fan': fan,
        'sport': sport,
    }
     
    return render(request, 'news/index.html', context)
def natija1(request):
    categories=Category.objects.all()
    return render(request, 'news/pages/404.html', {'category':categories})
def CategoryView(request):
    mahalliy = News.objects.filter(category_id=1)
    return render(request, 'news/pages/Category.html',{'mahalliy':mahalliy})

def PostDetail(request,id):
    news=get_object_or_404(News,id=id,status=News.Status.Published)
    yangilik3 = News.objects.all().order_by('-publish_time')[:3]
    categories=Category.objects.all()
    news.view_count = news.view_count+1
    news.save()
    url = 'https://v6.exchangerate-api.com/v6/b6944f9838eaa29e2ab310f5/pair/USD/UZS'
    url2 = "https://v6.exchangerate-api.com/v6/b6944f9838eaa29e2ab310f5/pair/EUR/UZS"
    url3 = "https://v6.exchangerate-api.com/v6/b6944f9838eaa29e2ab310f5/pair/RUB/UZS"
    res = requests.get(url)
    res2 = requests.get(url2)
    res3 = requests.get(url3)
    usd_uzs = int(res.json()['conversion_rate'])
    eur_uzs = int(res2.json()['conversion_rate'])
    rub_uzs = int(res2.json()['conversion_rate'])
    
    context = {
        'news': news,
        'yangilik3': yangilik3,
        'category': categories,  
        'usd_uzs': usd_uzs,
        'eur_uzs': eur_uzs,
        'rub_uzs': rub_uzs
    }
    return render(request, 'news/pages/single.html', context)

 
def newslist(request):
    news_list = News.objects.all()
    context = {
        'news_list': news_list
    }

    return render(request, 'news/news_list.html',context)


def contactpageview(request):
    form = contactform(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'news/pages/contact_done.html')
    categories=Category.objects.all()

    context = {
        'form': form,
        'category': categories
    }

    return render(request, 'news/pages/contact.html', context)

def successcontact(request):
    return render(request, 'news/pages/contact_done.html')


class Newscreatview(LoginRequiredMixin,CreateView):
    model = News
    template_name =  'news/news_create.html'
    fields = ('title','slug','body','image','category','status')
    raise_exception=True

class Newsupdateview(LoginRequiredMixin,UpdateView):
    model = News
    template_name = 'news/news_update.html'
    fields = ('title','slug','body','image','category','status')
    raise_exception=True

class Newsdelateview(LoginRequiredMixin,DeleteView):
    model = News
    template_name = 'news/news_delate.html'
    success_url = reverse_lazy('home')
    raise_exception=True


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('homepage')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm() 
    
    return render(
        request=request,
        template_name="news/login.html", 
        context={'form': form}
        )

def UserRegistr(request):
    if request.method == "POST":
        user_form = userregistrationform(request.POST)
        if user_form.is_valid():
            news_user = user_form.save(commit=False)
            news_user.set_password(user_form.cleaned_data["password1"])
            news_user.save()
            context = {
                "new_user": news_user,
            }
            return render(request, "news/pages/register_done.html",context)
    else:
        user_form = userregistrationform()
        context = {
            'user_form':user_form
            }
        return render(request,"news/pages/register.html",context)


