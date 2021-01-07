from django import forms

from photoclub.photos.models import Photo


class PhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Photo
        exclude = ('user',)
        # widgets = {
        #     'image_url': forms.TextInput(
        #         attrs={
        #             'id': 'img_new',
        #         })
        # }
