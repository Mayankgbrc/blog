from PIL import Image
from django import forms
from django.core.files import File
from .models import Photo
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,)
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(PhotoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Photo
        fields = ('file', 'x', 'y', 'width', 'height', )
    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        rgb_im = cropped_image.convert('RGB')
        file_name = 'blog/static/images/pic/' + str(self.user) + '.jpg'
        rgb_im.save(file_name)
        resized_image = rgb_im.resize((200, 200))
        resized_image.save('blog/static/images/thumbnail/'+str(self.user)+'.jpg')
        return photo