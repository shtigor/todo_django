from django import forms


class TODOForm(forms.Form):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control form-prettify',
                   'placeholder': 'You have 300 letters ...',
                   'maxlength': 300}), label=False)
