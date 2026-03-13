from django.contrib.auth.backends import ModelBackend
from .models import Participant

class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        
        try:
            user = Participant.objects.get(username= username)
        except Participant.DoesNotExist:
            try:
                user = Participant.objects.get(email=username)
            except Participant.DoesNotExist:
                return None
            
        if user.check_password(password):
            return user
        
        return None