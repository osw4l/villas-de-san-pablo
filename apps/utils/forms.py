from django import forms


class BaseFormAllFields(forms.ModelForm):
    title = None

    class Meta:
        model = None
        fields = '__all__'

