from django import forms
from Partida.models import Partida

class PartidaForm(forms.ModelForm):

    class Meta:
        model = Partida

        fields = [
            'Estado',
        ]
        labels = {
            'Estado':'Tamano del tablero',
        }
        widgets = {

            #'TamannoTablero':forms.TextInput(attrs={'type':'number','class':'form-control','min':'6','step':'0','placeholder':'Minimo 6'}),
            'Estado': forms.TextInput(attrs={'class':'form-control'}),
        }