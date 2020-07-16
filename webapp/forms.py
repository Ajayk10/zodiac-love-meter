from django import forms
from .models import *


class ContactForm(forms.ModelForm):
	class  Meta:
		model = Contact
		fields =["your_name","your_partner_name" ,"your_star","your_partner_star","feel","time"]   

