from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Post

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('myfirst.html')
  context = {
    'firstname': 'Connor'
  }
  return HttpResponse(template.render(context, request))

def modeltesting(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
    'greeting': 0,
  }
  return HttpResponse(template.render(context, request))

def homepage(request):
  myposts = Post.objects.all().values()
  template = loader.get_template('HomePage.html')
  context = {
    'myposts': myposts,
  }
  return HttpResponse(template.render(context, request))

def nhl(request):
  myposts = Post.objects.filter(sport_tag = 'NHL').values()
  template = loader.get_template('NHL.html')
  context = {
    'myposts': myposts,
  }
  return HttpResponse(template.render(context, request))

def nfl(request):
  myposts = Post.objects.filter(sport_tag = 'NFL').values()
  template = loader.get_template('NFL.html')
  context = {
    'myposts': myposts,
  }
  return HttpResponse(template.render(context, request))

def nba(request):
  myposts = Post.objects.filter(sport_tag = 'NBA').values()
  template = loader.get_template('NBA.html')
  context = {
    'myposts': myposts,
  }
  return HttpResponse(template.render(context, request))

def mlb(request):
  myposts = Post.objects.filter(sport_tag = 'MLB').values()
  template = loader.get_template('MLB.html')
  context = {
    'myposts': myposts,
  }
  return HttpResponse(template.render(context, request))

def golf(request):
  myposts = Post.objects.filter(sport_tag = 'Golf').values()
  template = loader.get_template('Golf.html')
  context = {
    'myposts': myposts,
  }
  return HttpResponse(template.render(context, request))