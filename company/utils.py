from app.models import Sponsor
from app.models import User

def context_addition(request, content):
    content['sponsor']=Sponsor.objects.filter(sponsor_id=User.objects.filter(id=request.user.id).first()).first()