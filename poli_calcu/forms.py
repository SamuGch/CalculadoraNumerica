from django import forms

class FuncionForm(forms.Form):
    funcion = forms.CharField(
        label='Función',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Escribe aquí la función. Ej. 2x^5 + 3 ...',
            'class': 'form-control'
        })
    )

    metodo = forms.ChoiceField(
        label='Método numérico',
        choices=[
            ('', '--- Selecciona un método ---'),
            ('biseccion', 'Bisección'),
            ('newton', 'Newton-Raphson'),
            ('newton_modificado', 'Newton-Raphson Modificado'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    a = forms.FloatField(
        label='Extremo inferior (a)',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 0'})
    )

    b = forms.FloatField(
        label='Extremo superior (b)',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 2'})
    )

    x0 = forms.FloatField(
        label='Valor inicial (x₀)',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1'})
    )

    tolerancia = forms.FloatField(
        label='Tolerancia',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 0.001'})
    )

    max_iter = forms.IntegerField(
        label='Máx iteraciones',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 100'})
    )
