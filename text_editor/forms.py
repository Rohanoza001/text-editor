from django import forms
from .models import Editor
from ckeditor.widgets import CKEditorWidget

class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = ['text']
        widgets = {
            'text': CKEditorWidget(),
        } 