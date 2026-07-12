from django import forms

class DataEntryVehiculoForm(forms.Form):
    de_image = forms.FileField(label="Archivo de Data Entry")