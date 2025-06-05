from sympy import symbols, lambdify

def bisection_method(func_expr, a, b, tol, max_iter):
    x = symbols('x')
    f = lambdify(x, func_expr, modules=["numpy"])

    if f(a) * f(b) >= 0:
        return None, "No se cumple la condición de cambio de signo", []

    iteraciones = []
    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        f_c = f(c)
        f_a = f(a)
        producto = f_a * f_c
        error = abs(b - a) / 2.0
        iteraciones.append({
            'No.': i,
            '(a)': a,
            '(b)': b,
            '(x)': c,
            'f(x)': f_c,
            'f(a)_f_(c)': producto,
            'Error': error
        })

        if abs(f_c) < tol or error < tol:
            return c, "Bisección", iteraciones

        if f(a) * f_c < 0:
            b = c
        else:
            a = c

    return c, "Máximo de iteraciones alcanzado", iteraciones
