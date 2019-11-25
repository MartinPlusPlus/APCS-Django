from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=100, widget=forms.Textarea)
    name = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        if "kyler" in name.lower():
            raise forms.ValidationError("Get out of here!")
