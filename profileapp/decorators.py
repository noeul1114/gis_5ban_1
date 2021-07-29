from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated
