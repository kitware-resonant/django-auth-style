from django.shortcuts import render

template_files = {
    'account_inactive.html': '/accounts/inactive/',
    'base.html': '/auth/base.html',
    'email.html': '/accounts/email/',
    'email_confirm.html': '/accounts/confirm-email/secret-key/',  # invalid?
    'login.html': '/accounts/login/',
    'logout.html': '/accounts/logout/',  # broken
    'password_change.html': '/accounts/password/change/',  # redirects
    'password_reset.html': '/accounts/password/reset/',
    'password_reset_done.html': '/accounts/password/reset/done/',
    'password_reset_from_key.html': '/accounts/password/reset/key/secret-key/',  # invalid?
    'password_reset_from_key_done.html': '/accounts/password/reset/key/done/',
    'password_set.html': '/accounts/password/set/',
    'signup.html': '/accounts/signup/',
    'signup_closed.html': '',
    'verification_sent.html': '/accounts/confirm-email/',
    'verified_email_required.html': '',
}


def auth_template_listing(request):
    return render(
        request,
        'girder_auth_design/auth_template_listing.html',
        {
            'template_files': template_files,
        },
    )


def auth_template(request, template_file):
    context = {}
    if template_file == 'password_reset_done.html':
        context['user'] = {
            'is_authenticated': True,
        }
    return render(request, f'account/{template_file}', context)
