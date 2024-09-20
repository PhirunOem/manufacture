import logging
from django.conf import settings
from django.shortcuts import redirect

class Check:
    def __init__(self, request):
        self.request = request
    def check_user_login(self):
        logger = logging.getLogger('django')
        logger.info('call func :::::::::::::::;')
        if not self.request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={self.request.path}") 