import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from app.models import *
from app.send_email import sendMail
from company.utils import *
from app.decorators import allowed_users

from .forms import SponserForm

group_cmp = 'Company'



@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def dashboardCmp(request):
    posts = InfluencerPost.objects.all().order_by("-id")
    nav_field = [i.field for i in posts]
    
    saved_posts = CmpSavePost.objects.filter(who_saved=Sponsor.objects.get(sponsor_id=User.objects.get(username=request.user.username)))
    saved_post_ls = [i.post.id for i in saved_posts]
    content = {
               'posts':posts,
               'nav_fields':list(set(nav_field)),
               'saved_post_ls':saved_post_ls
               }
    context_addition(request, content)                      
    return render(request, 'company/index.html', content)


   


@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def dashboardFilter(request):
    data = request.GET.get('object')
    if data == 'ALL': 
        posts = InfluencerPost.objects.all().order_by('-id')
    else:
        posts = InfluencerPost.objects.filter(field=data).order_by('-id')
    saved_posts = CmpSavePost.objects.filter(who_saved=Sponsor.objects.get(sponsor_id=User.objects.get(username=request.user.username)))
    saved_post_ls = [i.post.id for i in saved_posts]
    content = {'posts':posts,
               'saved_post_ls':saved_post_ls
               }           
    template = render_to_string('company/ajax_temp/dashboard_filter.html', content)
    return JsonResponse({'data': template})    


@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def saved_post_view(request):
    saved_posts = CmpSavePost.objects.filter(who_saved=Sponsor.objects.get(sponsor_id=User.objects.filter(username=request.user.username).first())).order_by("-id")
    print(saved_posts)
    saved_post_ls = [i.post.id for i in saved_posts]
    content = {'posts':saved_posts,
               'saved_post_ls':saved_post_ls,
               }
    context_addition(request, content)           
    return render(request, 'company/save_post.html', content)




@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def payment(request, post_id):
    post = InfluencerPost.objects.filter(id=post_id).first()
    if request.method == 'POST':
        Sponsored.objects.create(
            influencer=post.influencer,
            sponsor=Sponsor.objects.get(sponsor_id=User.objects.get(username=request.user.username)),
            mode_of_sponsorship='online',
            amount=post.price,
            transaction_id=random.randint(11111111, 99999999),
            complete=True,
            post=post
        )
        messages.success(request, 'Payment Successfully Done')
        return JsonResponse('Done', safe=True)
    content = {'post':post, 'id':post_id}
    context_addition(request, content)
    return render(request, 'company/payment.html', content)


@login_required(login_url='login')
def transaction(request):
    sponsor = Sponsor.objects.get(sponsor_id=User.objects.get(username=request.user.username))
    sponsored_details = Sponsored.objects.filter(sponsor=sponsor)
    content = {'sponsored_details': sponsored_details, 'sponsor': sponsor}
    return render(request, 'company/transaction.html', content)





@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def sponsored(request):
    sponsor = Sponsor.objects.get(sponsor_id=User.objects.get(username=request.user.username))
    sponsored_details = Sponsored.objects.filter(sponsor=sponsor)
    posts = [i.post for i in sponsored_details]
    content = {'posts':posts}
    context_addition(request, content)
    return render(request, 'company/history.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def accept_mail(request, id):
    post = InfluencerPost.objects.filter(id=id).first()
    sponsor = Sponsor.objects.get(sponsor_id=User.objects.get(username=request.user.username))
    content = {
        'post':post,
        'sponsor':sponsor
    }
    sendMail(request,email=[post.influencer.influencer_id.email],mailFor=content ,msg='acceptDeal', subject='Sponsorship Acceptance')
    messages.success(request, 'Send Successfully')
    return redirect('dashboardCmp')


@login_required(login_url='login')
@allowed_users(allowed_roles=[group_cmp])
def creation(request):
    form=SponserForm()
    if request.method=="POST":
        form=SponserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboardCmp")
    content={"form":form}
    return render(request,"company/creation.html",content)


@login_required(login_url='login')
def profile_cmp(request, id):
    influencer = Influencer.objects.get(id=id)
    socialmedia = InfSocialMedia.objects.filter(influencer=influencer)
    content = {'socialmedia':socialmedia, 'influencer':influencer}
    return render(request, 'company/profile/profile.html', content)

@login_required(login_url='login')
def personal_post_cmp(request, id):
    influencer = Influencer.objects.get(id=id)
    posts = InfluencerPost.objects.filter(influencer=influencer)
    content = {'influencer':influencer, 'posts':posts}
    return render(request, 'company/profile/post.html', content)


