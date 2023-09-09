from django import forms

class UploadImageForm(forms.Form):
    image = forms.ImageField()

class SettingsForm(forms.Form):
    conversion_method = forms.ChoiceField(choices=[
        ('method_1', 'Method 1'),
        ('method_2', 'Method 2'),
        ('method_3', 'Method 3'),
    ])
    adjustment_level = forms.IntegerField(min_value=1, max_value=10)