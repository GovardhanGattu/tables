from django.forms import ModelForm

from tables.models import Table

class Mytable(ModelForm):
	class Meta:
		model=Table
		fields='__all__' #['name','phno']