from django import forms


class BaseFormAllFields(forms.ModelForm):
    class Meta:
        model = None
        fields = '__all__'

