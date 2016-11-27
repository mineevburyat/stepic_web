from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        ask = Question(**self.cleaned_data)
        ask.save()
        return ask

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=100)
    question = forms.ModelChoiceField(Question.objects.all())

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

