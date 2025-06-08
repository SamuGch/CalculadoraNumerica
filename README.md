# Calculadora Numérica

**Calculadora Numérica** es una aplicación web interactiva que permite ingresar funciones matemáticas y calcular sus raíces utilizando distintos métodos numéricos. Fue desarrollada con Python y Django, con una interfaz construida con Bootstrap.

## 1. Funcionalidad

- Ingreso de funciones a través de un formulario dinámico.
- Selección de método numérico:
  - Método de Bisección
  - Método de Newton-Raphson
  - Método de Newton-Raphson Modificado
- Campos del formulario adaptables según el método seleccionado. Pudiendo ser
  - Valores a b 
  - Valoe inicial X0
  - Valor de Tolerancia
  - MAximi de iteraciones
- Cálculo de la raíz y presentación de:
  - Función utilizada
  - Raíz encontrada
  - Tabla de iteraciones
  - Gráfica del polinomio con el punto raíz resaltado
- Navegación entre páginas con opción para volver al formulario inicial.

## 2. Tecnologías y librerías utilizadas

- **Backend:** Django
- **Frontend:** Bootstrap
- **Cálculos y visualización:**
  - `numpy` – para operaciones numéricas
  - `sympy` – para el manejo simbólico de funciones
  - `matplotlib` – para graficar las funciones y raíces

> 3. Proyecto desarrollado en el entorno de trabajo **PyCharm**.

##  Instalación

1. Clona el repositorio:
   ```bash
   git clone https:https://github.com/SamuGch/CalculadoraNumerica
   cd calculadora-numerica
