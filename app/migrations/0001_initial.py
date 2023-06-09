# Generated by Django 3.2.7 on 2021-11-09 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(choices=[('Comedy', 'Comedy'), ('Commentary', 'Commentary'), ('Educational', 'Educational'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Gaming', 'Gaming'), ('Interview', 'Interview'), ('Music', 'Music'), ('ProductReview', 'ProductReview'), ('Q&A', 'Q&A'), ('Reaction', 'Reaction'), ('Sport', 'Sport'), ('Travel', 'Travel')], max_length=50)),
                ('profileImg', models.ImageField(upload_to='profileImg/influencer/')),
                ('dob', models.DateField()),
                ('phone_no', models.CharField(max_length=13)),
                ('bio', models.TextField(max_length=300)),
                ('location', models.CharField(max_length=200)),
                ('pancard', models.CharField(default='NA', max_length=12, null=True)),
                ('mode_of_transaction', models.CharField(choices=[('1', 'NetBanking'), ('2', 'Card'), ('3', 'UPI'), ('4', 'Other')], default='NA', max_length=25)),
                ('bank_name', models.CharField(default='NA', max_length=25, null=True)),
                ('IFSC_code', models.CharField(default='NA', max_length=15, null=True)),
                ('account_no', models.CharField(default='NA', max_length=15, null=True)),
                ('is_verified', models.BooleanField(default=False, null=True)),
                ('influencer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InfluencerPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('price_desc', models.TextField(max_length=500, null=True)),
                ('day', models.IntegerField(blank=True, default=5, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('field', models.CharField(choices=[('Comedy', 'Comedy'), ('Commentary', 'Commentary'), ('Educational', 'Educational'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Gaming', 'Gaming'), ('Interview', 'Interview'), ('Music', 'Music'), ('ProductReview', 'ProductReview'), ('Q&A', 'Q&A'), ('Reaction', 'Reaction'), ('Sport', 'Sport'), ('Travel', 'Travel')], max_length=50)),
                ('adfield', models.CharField(choices=[('Facebook Post', 'Facebook Post'), ('Facebook Story + Swipe Up', 'Facebook Story + Swipe Up'), ('Instagram Post', 'Instagram Post'), ('Instagram Reels', 'Instagram Reels'), ('Instagram Story + Swipe Up', 'Instagram Story + Swipe Up'), ('Tiktok Video', 'Tiktok Video'), ('YouTube Shorts + Swipe Up', 'YouTube Shorts + Swipe Up'), ('YouTube Video', 'YouTube Video')], max_length=50, null=True)),
                ('post_img', models.ImageField(upload_to='post/influencer/')),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.influencer')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(choices=[('Comedy', 'Comedy'), ('Commentary', 'Commentary'), ('Educational', 'Educational'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Gaming', 'Gaming'), ('Interview', 'Interview'), ('Music', 'Music'), ('ProductReview', 'ProductReview'), ('Q&A', 'Q&A'), ('Reaction', 'Reaction'), ('Sport', 'Sport'), ('Travel', 'Travel')], max_length=50)),
                ('profile_img', models.ImageField(upload_to='profileImg/sponsor/')),
                ('pancard', models.CharField(max_length=12, null=True)),
                ('cin_no', models.CharField(max_length=21, null=True)),
                ('phone_no', models.CharField(max_length=13)),
                ('address', models.TextField(max_length=300)),
                ('website_link', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('other_link', models.URLField(null=True)),
                ('is_verified', models.BooleanField(default=False, null=True)),
                ('sponsor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsored',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_of_sponsorship', models.CharField(choices=[('online', 'online')], max_length=50)),
                ('transaction_id', models.CharField(max_length=50)),
                ('amount', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.influencer')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.influencerpost')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='InfSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True)),
                ('social_media', models.CharField(max_length=100, null=True)),
                ('followers', models.CharField(max_length=30, null=True)),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.influencer')),
            ],
        ),
        migrations.CreateModel(
            name='InfSavePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.influencerpost')),
                ('who_saved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.influencer')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_link', models.URLField(null=True)),
                ('is_accepted', models.BooleanField()),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.influencer')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.influencerpost')),
            ],
        ),
        migrations.CreateModel(
            name='CmpSavePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.influencerpost')),
                ('who_saved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sponsor')),
            ],
        ),
    ]
