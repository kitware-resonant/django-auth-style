from django.shortcuts import render
from django.urls import reverse_lazy

reverse_lazy('')

template_files = {
    'account_inactive.html': reverse_lazy('account_inactive'),
    'base.html': None,
    'email.html': reverse_lazy('account_email'),
    'email_confirm.html': reverse_lazy(
        'account_confirm_email', kwargs={'key': 'secret-key'}
    ),  # invalid?
    'login.html': reverse_lazy('account_login'),
    'logout.html': reverse_lazy('account_logout'),  # broken
    'password_change.html': reverse_lazy('account_change_password'),  # redirects
    'password_reset.html': reverse_lazy('account_reset_password'),
    'password_reset_done.html': reverse_lazy('account_reset_password_done'),
    'password_reset_from_key.html': reverse_lazy(
        'account_reset_password_from_key', kwargs={'uidb36': '0', 'key': 'secret-key'}
    ),  # invalid?
    'password_reset_from_key_done.html': reverse_lazy('account_reset_password_from_key_done'),
    'password_set.html': reverse_lazy('account_set_password'),
    'signup.html': reverse_lazy('account_signup'),
    'signup_closed.html': None,
    'verification_sent.html': reverse_lazy('account_email_verification_sent'),
    'verified_email_required.html': None,
}


def auth_template_listing(request):
    return render(
        request,
        'girder_auth_design/auth_template_listing.html',
        {
            'template_files': template_files,
        },
    )


def auth_template_file(request, template_file):
    # TODO: This is not used yet
    context = {}
    if template_file == 'password_reset_done.html':
        context['user'] = {
            'is_authenticated': True,
        }
    return render(request, f'account/{template_file}', context)
