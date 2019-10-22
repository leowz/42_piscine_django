from django import forms

class MyForm(forms.Form):
	def __init__(self, titleChoices, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['films'] = forms.ChoiceField(choices=[(str(o), str(o)) for o in titleChoices])
		print(self.fields);