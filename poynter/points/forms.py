from django import forms

from poynter.points.models import Vote


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ("vote",)
