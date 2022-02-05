from django import forms
from pro1.models import Post,Comment
from django.core.validators import MaxValueValidator, MinValueValidator

# Defining the music choices. Tuples given. Pass this into the widgets for the Meta of PostForm.
# Note: The form classes inherit from the ModelForm, which uses the models we created, and specified fields
Music_choices = [('Acoustic','Acoustic'),
                ('Old School','Old School'),
                ('Modern Country','Modern Country'),
                ('Irish Country','Irish Country'),
                ('Guitar Based','Guitar Based'),
                ('Other','Other')]


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'type','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'type':forms.Select(choices=Music_choices) # Pass in list of choices
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text','rating') # Selected fields.

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
