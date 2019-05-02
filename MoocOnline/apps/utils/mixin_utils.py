# _*_ coding: utf-8 _*_
__author__ = 'Ren Tingsong'
__date__ = '2019/3/26 0026 上午 9:53'


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
