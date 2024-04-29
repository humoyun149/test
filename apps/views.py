from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.db.models import Q, Count
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from apps.models import Blog, Category


# class IndexListView(ListView):
#     queryset = Contact.objects.all()
#     template_name = 'apps/index.html'
#     context_object_name = 'contacts'
#     print('hello worlds')
#
#     def get_queryset(self):
#         category_id = self.request.GET.get('country')
#         queryset = Contact.objects.all()
#         if category_id:
#             queryset = queryset.filter(category_id=category_id)
#         return queryset
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_lipostst, **kwargs)
#         context['country'] = Country.objects.all()
#         return context


# def list_view(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#         'categories': Category.objects.all()
#     }
#     return render(request, 'apps/blog-list-left-sidebar.html', context)


class HomeView(TemplateView):
    template_name = 'apps/index.html'


class BlogListView(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'products'
    template_name = 'apps/blog-list-left-sidebar.html'
    paginate_by = 2

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        search = self.request.GET.get('search')
        queryset = super().get_queryset()
        if search:
            queryset = queryset.filter(Q(title__icontains=search), Q(description__icontains=search))
        if category_id:
            queryset = queryset.filter(category=category_id)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        categories = Category.objects.prefetch_related('blog_set').annotate(blog_count=Count('blog__id'))
        context['categories'] = categories

        return context


def detail_view(request, pk):
    product = Blog.objects.get(pk=pk)
    categories = Category.objects.prefetch_related('blog_set').annotate(blog_count=Count('blog__id'))
    context = {
        'product': product,
        'categories': categories
    }
    return render(request, 'apps/blog-details-left-sidebar.html', context)


def send_email_view(recipient, text: str):
    subject = 'Account created successfully'
    message = text
    recipient_list = [recipient]
    EMAIL_HOST_USER = 'humoyun17121965@gmail.com'
    send_mail(subject, message, EMAIL_HOST_USER, recipient_list)


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
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
                                                    first_name=first_name,
                                                    last_name=last_name)
                    user.save()
                    send_email_view(email, f'{username} nomli account yaratildi ')
                    messages.success(request, 'Account created successfully')
                    return redirect('register_view')
            else:
                messages.info(request, 'Confirm password error')
                return redirect('register_view')
        else:
            messages.info(request, 'Password or Username empty')
            return redirect('register_view')
    else:
        return render(request, 'apps/login-register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home/')
        else:
            login = messages.info(request, 'Login Not found')
            return redirect('register_view')
    else:
        return render(request, 'apps/login-register.html')


class CustomLoginView(LoginView):
    template_name = 'apps/login-register.html'
    next_page = 'blog_list'
