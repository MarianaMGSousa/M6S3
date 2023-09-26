from django import forms
from base.models import Contato, Reserva

class ContatoForm(forms.ModelForm):
    class Meta:
        # Definir o modelo do formulário
        model = Contato
        
        # Definir os campos do formulário
        fields = ['nome', 'email', 'mensagem']
        
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu nome'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder':'Insira seu email'
                }
            ),
            'mensagem': forms.Textarea(
                attrs={
                    'placeholder': 'Insira sua mensagem'
                }
            ),
        }
        
        # Definir os "titulos dos campos"
        labels = {
            'nome': 'Nome:',
            'email': 'E-mail:',
            'mensagem': 'Mensagem:',
        }
    

class DateInput(forms.DateInput):
    input_type = 'date'


class ReservaForm(forms.ModelForm):
    class Meta:
        # Definir o modelo do formulário
        model = Reserva
        
        # Definir os campos do formulário
        fields = ['nome_pet', 'telefone', 'data_reserva', 'observacoes']
        
        widgets = {
            'nome_pet': forms.TextInput(
                attrs={
                    'placeholder': 'Insira o nome do seu pet'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'placeholder':'Insira seu telefone'
                }
            ),
            'data_reserva': DateInput(),
            
            'observacoes': forms.Textarea(
                attrs={
                    'placeholder': 'Insira sua observação'
                }
            ),
        }
        
        # Definir os "titulos dos campos"
        labels = {
            'nome_pet': 'Nome do Pet:',
            'telefone': 'Telefone:',
            'data_reserva': 'Data da reserva',
            'observações': 'Observações:',
        }