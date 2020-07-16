from django.shortcuts import render , redirect
from . models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from datetime import datetime
from django.contrib import messages

# Create your views here.



def home(request):
	return render(request, "home.html" ,{})

def prediction(request):
	if request.method == 'POST':
		form = ContactForm(request.POST or None)
		if form.is_valid():
			form.save()
		item=Contact.objects.all

		global curr_name,curr_partner,curr_star,curr_partner_star,sun,moon,mercury,venus,jupiter,saturn,mars
		global string,string2,feel,percent
		curr_name=request.POST.get('your_name').lower()
		curr_partner=request.POST.get('your_partner_name').lower()
		curr_star=request.POST.get('your_star').lower()
		curr_partner_star=request.POST.get('your_partner_star').lower()
		feel=request.POST.get('feel')

		compat=curr_name+curr_partner
		for c in compat:
		    compname = ord(c)
		    compvalue =compname//3


		star=curr_star+curr_partner_star
		for s in star:
		    starname = ord(s)
		    value =starname//3


		#star-relationship
		sibling = (1,8, 16, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97)
		friend = (2, 10, 18,72, 80, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98)
		bestfriend = (3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99)
		lover = (4, 12,24, 32, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100)
		partner = (5, 13, 21,56, 64, 29, 37, 45, 53, 61, 69, 77, 85, 93)
		marg = (6, 14, 22,40, 48, 30, 38, 46, 54, 62, 70, 78, 86, 94)
		affair = (7, 15, 23, 31,88, 96, 39, 47, 55, 63, 71, 79, 87, 95)

		if value in sibling:
		    string="Based on the Sign you both have Sister/Brother relationship"
		    jupiter=1
		    mars=3
		    venus=5
		    mercury=6
		    percent=5

		elif value in friend:
		    string="Based on the Sign you both will be good Friends"
		    jupiter = 3
		    mars = 4
		    venus = 5
		    mercury = 12
		    percent=6

		elif value in bestfriend:
		    string="Based on the Sign you both will be thick Best Friend"
		    jupiter = 3
		    mars = 6
		    venus = 5
		    mercury = 2
		    percent=7

		elif value in lover:
		    string="Based on the Sign you together have chances to be awesome Lovers"
		    jupiter = 4
		    mars = 5
		    venus = 11
		    mercury = 4
		    percent=8

		elif value in partner:
		    string="Based on the Sign you together have bondings to be Partner"
		    jupiter = 4
		    mars = 5
		    venus = 10
		    mercury = 1
		    percent=9

		elif value in marg:
		    string="Based on the Sign you together have bondings of a Husband-Wife"
		    jupiter = 2
		    mars = 8
		    venus = 4
		    mercury = 3
		    percent=9

		elif value in affair:
		    string="Based on the Sign you both can have an secretive relationship together simialar to an Affair"
		    jupiter = 9
		    mars = 3
		    venus = 8
		    mercury = 11
		    percent=7

		#name-intimacy
		crush = (1,8, 16, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97)
		fantasy = (2, 10, 18,72, 80, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98)
		slight_love = (3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99)
		deep_love = (4, 12,24, 32, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100)
		one_night_stand = (5, 13, 21,56, 64, 29, 37, 45, 53, 61, 69, 77, 85, 93)
		till_death= (6, 14, 22,40, 48, 30, 38, 46, 54, 62, 70, 78, 86, 94)
		infactuation = (7, 15, 23, 31,88, 96, 39, 47, 55, 63, 71, 79, 87, 95)
		if compvalue in crush:
		    string2="and Nameology says you both have crush on each other"
		    moon = 3
		    sun = 7
		    saturn = 6


		elif compvalue in fantasy:
		    string2="and Nameology says that you both fantasise each other atleast once in a week,month or year"
		    moon = 4
		    sun = 9
		    saturn = 8

		elif compvalue in slight_love:
		    string2="and Nameology says there are slight chances for you both to fall in love"
		    moon = 5
		    sun = 2
		    saturn = 6

		elif compvalue in deep_love:
		    string2="and Nameology says that you both are in deeply love with eachother but may be not admitting it"
		    moon = 1
		    sun = 12
		    saturn = 6

		elif compvalue in one_night_stand:
		    string2="and Nameology says you both are willing for one night stand with eachother"
		    moon = 9
		    sun = 11
		    saturn = 7

		elif compvalue in till_death:
		    string2="and Nameology says you both will be together till last of the life "
		    moon = 7
		    sun = 12
		    saturn = 8

		elif compvalue in infactuation:
		    string2="and Nameology says you both have an infactuation on eachother "
		    moon = 9
		    sun = 11
		    saturn = 2


		messages.success(request,'The Result between '+curr_name+' and '+curr_partner+ ' is ready..')

		return render(request, 'prediction.html' ,{'item':item})
	else:
		item=Contact.objects.all
		return render(request, 'prediction.html' ,{'item':item})


def result(request):
	try:
		zodiac = ('aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces')
		if curr_star in zodiac and curr_partner_star in zodiac:
		    all_item=Contact.objects.all
		    messages.success(request,curr_name+' and '+curr_partner)
		    context = {'sun':sun,'moon':moon,'mercury':mercury,'venus':venus,
				'mars':mars,'jupiter':jupiter,'saturn':saturn,'string':string,'string2':string2,
				'all_item':all_item,'curr_star':curr_star,'curr_name':curr_name,'curr_partner':curr_partner
				,'percent':percent}
		    return render(request, "result.html" ,context)
		else:
		    messages.warning(request,"Enter the correct Zodiac star name the entered value is inavalid..!!")
		    return render(request, "result.html")
	except NameError:
		return render(request, "error.html")
		

def mypanel(request):
	all_item=Contact.objects.all
	return render(request, "mypanel.html" ,{'all_item':all_item})

def error(request):
	return render(request, "error.html" ,{})


