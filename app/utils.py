import re
from .models import Influencer, User

def password_val(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    c_pass = re.compile(regex)
    matrix = re.search(c_pass, password)

    return matrix

def context_addition(request, content):
    influencer_id = User.objects.get(id=request.user.id)
    content['influencer']=Influencer.objects.filter(influencer_id=influencer_id).first()
    content['all_influencer']=Influencer.objects.all()[:8]