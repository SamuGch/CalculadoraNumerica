from django.shortcuts import render
from django.conf import settings
from .forms import FuncionForm
from .metodos_numericos.bisection import bisection_method
from .metodos_numericos.newton import newton_method
from .metodos_numericos.newton_modificado import newton_mod_method
from sympy import sympify, symbols, lambdify
import matplotlib.pyplot as plt
import numpy as np
import os
import re

def generar_grafica(expr, xmin=-10, xmax=10, raiz=None):
    x = symbols('x')
    f = lambdify(x, expr, modules=['numpy'])
    x_vals = np.linspace(xmin, xmax, 400)
    y_vals = f(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color='green', linestyle='--')

    if raiz is not None:
        try:
            y_raiz = f(raiz)
            plt.plot(raiz, y_raiz, 'ro', label=f'Raíz ≈ {raiz:.4f}')
        except Exception as e:
            print("Error al graficar la raíz:", e)

    plt.title('Gráfica del Polinomio')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)

    path = os.path.join(settings.MEDIA_ROOT, 'plot.png')
    plt.savefig(path)
    plt.close()

def index(request):
    if request.method == 'POST':
        form = FuncionForm(request.POST)
        if form.is_valid():
            funcion_raw = form.cleaned_data['funcion']
            metodo = form.cleaned_data['metodo']
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            x0 = form.cleaned_data.get('x0')
            tol = form.cleaned_data['tolerancia']
            max_iter = form.cleaned_data['max_iter']

            funcion = funcion_raw.replace('^', '**')
            funcion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion)
            funcion = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', funcion)

            try:
                expr = sympify(funcion)
            except Exception as e:
                return render(request, 'poli_calcu/index.html', {
                    'form': form,
                    'error': f'Error al interpretar la función: {e}'
                })

            resultado = None
            mensaje = ""
            iteraciones = []

            try:
                if metodo == 'biseccion':
                    if a is None or b is None:
                        raise ValueError('Debes ingresar los valores de a y b.')
                    x = symbols('x')
                    f = lambdify(x, expr, modules=['numpy'])
                    if f(a) * f(b) >= 0:
                        raise ValueError('No se cumple la condición de cambio de signo: f(a) * f(b) debe ser < 0.')
                    resultado, mensaje, iteraciones = bisection_method(expr, a, b, tol, max_iter)

                elif metodo == 'newton':
                    if x0 is None:
                        raise ValueError('Debes ingresar el valor inicial x₀.')
                    resultado, mensaje, iteraciones = newton_method(expr, x0, tol, max_iter)

                elif metodo == 'newton_modificado':
                    if x0 is None:
                        raise ValueError('Debes ingresar el valor inicial x₀.')
                    resultado, mensaje, iteraciones = newton_mod_method(expr, x0, tol, max_iter)

                else:
                    raise ValueError('Método no reconocido.')

                generar_grafica(expr, raiz=resultado if isinstance(resultado, (int, float, float)) else None)

                tabla_headers = list(iteraciones[0].keys()) if iteraciones else []
                tabla_datos = [list(fila.values()) for fila in iteraciones]

                return render(request, 'poli_calcu/results.html', {
                    'funcion': str(expr),
                    'resultado': resultado,
                    'mensaje': mensaje,
                    'tabla_headers': tabla_headers,
                    'tabla_datos': tabla_datos
                })

            except Exception as e:
                return render(request, 'poli_calcu/index.html', {
                    'form': form,
                    'error': str(e)
                })

    else:
        form = FuncionForm()

    return render(request, 'poli_calcu/index.html', {'form': form})

