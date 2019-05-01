from django import forms


class ContactForm(forms.Form):
    SENTIMENT_OPTIONS = (
        ('Positive', 'Positive Overall'),
        ('Negative', 'Negative Overall')
    )

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)
    sentiment = forms.ChoiceField(required=True, choices=SENTIMENT_OPTIONS)
