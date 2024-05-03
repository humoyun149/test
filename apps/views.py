from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from apps.models import People
from apps.tasks import send_to_user_email


class PeopleListView(ListView):
    queryset = People.objects.all()
    context_object_name = 'people'
    template_name = 'apps/index.html'
    paginate_by = 3


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password and password2 and username:
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username taken')
                    return redirect('register_view')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password,
                                                    first_name=first_name)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login_view')
            else:
                messages.info(request, 'Confirm password error')
                return redirect('register_view')
        else:
            messages.info(request, 'Password or Username empty')
            return redirect('register_view')
    else:
        return render(request, 'apps/register.html')


class UserLoginView(LoginView):
    template_name = 'apps/login_view.html'
    next_page = 'index_view'


def detail_view(request, pk):
    people = People.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        people.name = name
        people.email = email
        people.address = address
        people.save()
    context = {
        "people": people
    }
    return render(request, 'apps/detail_view.html', context=context)


# ///////////////////////////////////////////////////////////////////////////////////
def send_email_to_user(request):
    email = request.GET.get('email')
    msg = request.GET.get('msg')
    send_to_user_email.delay(email, msg)
    return HttpResponse('Hello, world')
# ///////////////////////////////////////////////////////////////////////////////////
