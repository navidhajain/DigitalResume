from django.contrib.auth.models import User

def project_context(requests):
    context={
        'me': User.objects.first(),
    }

    return context

