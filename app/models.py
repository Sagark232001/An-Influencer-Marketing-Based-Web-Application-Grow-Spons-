from django.db import models
from django.contrib.auth.models import User

# In user Email id and User are same

fields_list=sorted({
    ("Commentary","Commentary"),("ProductReview","ProductReview"),("Comedy","Comedy"),("Reaction","Reaction"),("Q&A","Q&A"),("Interview","Interview"),("Educational","Educational"),("Music","Music"),("Gaming","Gaming"),("Sport","Sport"),("Food","Food"),("Fashion","Fashion"),("Travel","Travel"), ("Fitness", "Fitness")
})

adfields_list=sorted({
    ("Instagram Story + Swipe Up","Instagram Story + Swipe Up"),("Instagram Post","Instagram Post"),("Instagram Reels","Instagram Reels"),("Facebook Story + Swipe Up","Facebook Story + Swipe Up"),("Instagram Post","Instagram Post"),("Facebook Post","Facebook Post"),("YouTube Shorts + Swipe Up","YouTube Shorts + Swipe Up"), ("YouTube Video","YouTube Video")
})



class Sponsor(models.Model):
    sponsor_id=models.OneToOneField(User,on_delete=models.CASCADE)
    field=models.CharField(max_length=50,choices=fields_list)
    profile_img=models.ImageField(upload_to="profileImg/sponsor/")
    pancard=models.CharField(max_length=12,null=True)
    cin_no=models.CharField(max_length=21,null=True)
    phone_no=models.CharField(max_length=13)
    address=models.TextField(max_length=300)
    website_link=models.URLField(null=True)
    facebook=models.URLField(null=True)
    instagram=models.URLField(null=True)
    twitter=models.URLField(null=True)
    other_link=models.URLField(null=True)
    is_verified=models.BooleanField(null=True,default=True)

    def __str__(self):
        return str(self.sponsor_id.username)

class Influencer(models.Model):
    influencer_id=models.OneToOneField(User,on_delete=models.CASCADE)
    field=models.CharField(max_length=50,choices=fields_list)
    profileImg=models.ImageField(upload_to="profileImg/influencer/")
    dob = models.DateField()
    phone_no=models.CharField(max_length=13)
    bio=models.TextField(max_length=300)
    location=models.CharField(max_length=200)
    
    pancard=models.CharField(max_length=12,null=True, default='NA')
    mode_of_transaction=models.CharField(max_length=25, default='NA', choices=sorted({
        ("1","NetBanking"),("2","Card"),("3","UPI"),("4","Other")
    }))
    bank_name=models.CharField(max_length=25,null=True, default='NA')
    IFSC_code=models.CharField(max_length=15,null=True, default='NA')
    account_no=models.CharField(max_length=15,null=True, default='NA')

    is_verified=models.BooleanField(null=True, default=True)

    def __str__(self):
        return str(self.influencer_id.username)

class InfSocialMedia(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    url = models.URLField(null=True)
    social_media = models.CharField(max_length=100, null=True)
    followers = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.influencer.influencer_id.username)


class InfluencerPost(models.Model):
    influencer=models.ForeignKey(Influencer,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    price=models.IntegerField(null=True, blank=True, default=0)
    price_desc=models.TextField(max_length=500,null=True)
    day=models.IntegerField(null=True, blank=True, default=5)
    description=models.TextField(max_length=500,null=True)
    field=models.CharField(max_length=50,choices=fields_list)
    adfield=models.CharField(max_length=50,choices=adfields_list,null=True)
    post_img=models.ImageField(upload_to="post/influencer/")

    def __str__(self):
        return str(self.title)+","+str(self.influencer)


class InfSavePost(models.Model):
    who_saved = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    post = models.ForeignKey(InfluencerPost, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class CmpSavePost(models.Model):
    who_saved = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=True)    # later change to Sponser
    post = models.ForeignKey(InfluencerPost, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Content(models.Model):
    influencer=models.ForeignKey(Influencer,on_delete=models.CASCADE)
    post=models.ForeignKey(InfluencerPost, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    content_link=models.URLField(null=True, blank=True)
    is_accepted=models.BooleanField()
    def __str__(self):
        return str(self.influencer.influencer_id.username)

class Sponsored(models.Model):
    influencer=models.ForeignKey(Influencer,on_delete=models.CASCADE)
    post=models.ForeignKey(InfluencerPost, on_delete=models.CASCADE, null=True)
    sponsor=models.ForeignKey(Sponsor,on_delete=models.CASCADE)
    mode_of_sponsorship=models.CharField(max_length=50,choices=sorted({
        ('online','online')
    }))
    transaction_id=models.CharField(max_length=50)
    amount=models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.transaction_id)

