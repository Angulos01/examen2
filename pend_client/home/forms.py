from django import forms

CHOICES_PRIORITY = (
    ("ALTA", "ALT"),
    ("MEDIA", "MD"),
    ("BAJA", "BJ"),
)

CHIOCES_STATE = (
    ("SIN_RESOLVER", "Sin resolver"),
    ("PENDIENTE", "Pendiente"),
    ("RESUELTO", "Resuelto"),
)

class CreatePendienteForm(forms.Form):
        title = forms.CharField(max_length=32, widget= forms.TextInput(attrs={"type":"text", "class":"form-control"}))
        description= forms.CharField(max_length=32, widget= forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3}))
        priority= forms.CharField(max_length=16,widget=(forms.Select(choices=CHOICES_PRIORITY,attrs={'type':'select','class':'form-select'})))
        state = forms.CharField(max_length=16,widget=(forms.Select(choices=CHIOCES_STATE,attrs={'type':'select','class':'form-select'})))
        status = forms.BooleanField(initial=True)

