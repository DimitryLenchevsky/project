from django.contrib.auth.views import LoginView, PasswordChangeView


class MyLogin(LoginView):
    template_name = 'auth/login.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'auth/password_change.html'
    success_url = '/products/templates/list.html/'
