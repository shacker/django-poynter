from django import forms

from poynter.points.models import Vote, Ticket


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ("vote",)


class TicketForm(forms.ModelForm):
    """ Used in the Admin to validate one active ticket per session.
    self is the form; instance is the ticket.
    """
    class Meta:
        model = Ticket
        fields = '__all__'

    def clean(self):

        cleaned_data = super().clean()
        space = cleaned_data.get("space")
        if self.instance.active and space.ticket_set.exclude(id=self.instance.id).filter(active=True):
            raise forms.ValidationError(
                "Another ticket is already listed as active in this Space. "
                "Set others to Unknown before changing this one."
            )
        return self.cleaned_data
