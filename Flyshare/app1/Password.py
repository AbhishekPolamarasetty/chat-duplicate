from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

class CustomPasswordResetView(PasswordResetView):
    template_name = 'Login/password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = '/password_reset_done/'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'Login/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'Login/password_reset_confirm.html'
    success_url = '/reset/done/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'Login/password_reset_complete.html'
