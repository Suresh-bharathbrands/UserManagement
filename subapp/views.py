from django.shortcuts import render,redirect
from django.http import  HttpResponseRedirect
from subapp.models import *
from subapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required()
def item_save(request):
    view = Item.objects.all()
    form=ItemForm()
    if request.method=='POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return HttpResponseRedirect('/item_save')
    context={
        'form':form,"view":view
        }
    return render(request, 'item_save.html',context)

@login_required()
def item_edit(request,pk):
    view = Item.objects.all()
    record = Item.objects.get(id=pk)
    form=ItemForm(instance=record)
    if request.method=='POST':
        form=ItemForm(request.POST,instance=record)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return HttpResponseRedirect('/item_save')
    context={
        'form':form,"view":view
        }
    return render(request, 'item_save.html',context)
@login_required()
def item_delete(request,pk):
    Item.objects.get(id=pk).delete()
    return HttpResponseRedirect('/item_save')

def user_profile(request):
    records=UserProfile.objects.all()
    return render(request,'user_profile.html',{'records':records})
def user_profile_save(request):
    if request.method=='POST':
        UserProfile.objects.create(
            profile_name=request.POST.get('profile_name'),
            screen_access=request.POST.getlist('access'),
        )
        return redirect('user_profile')
    return render(request,'user_profile_save.html')

def user_view(request):
    records=CreateUser.objects.all()
    context = {
        'records': records
    }
    return render(request,'user_view.html',context)

def user_create(request):
    userform = UserForm()
    createuserform = CreateUserForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        createuserform = CreateUserForm(request.POST)
        if userform.is_valid() and createuserform.is_valid():
            userform.save()
            data=createuserform.save(commit=False)
            user_record=User.objects.get(username=request.POST.get('username'))
            data.user=user_record
            data.save()
            return redirect('user_view')
        
    context = {
        'userform': userform,'createuserform':createuserform
    }
    return render(request,'user_create.html',context)

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')