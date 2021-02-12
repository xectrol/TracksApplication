from django import forms


class GenreForm(forms.Form):
    genre = forms.CharField(required=True,
                            max_length=18,
                            widget=forms.TextInput(attrs={'class': "input"}))

    def clean_genre(self):
        data = self.cleaned_data.get('genre')
        if data is not None and data != 'rock' and data != 'pop' and data != 'alternative rock' and data != 'blues' and data != 'country' and \
                data != 'electronic' and data != 'jazz' and data != 'r&b' and data != 'rap' and data != 'reggae':
            raise forms.ValidationError("Please make sure you entered the correct genre")

        return data

