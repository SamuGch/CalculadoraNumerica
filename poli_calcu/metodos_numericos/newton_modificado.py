from sympy import diff, symbols, lambdify

def newton_mod_method(func_expr, x0, tol, max_iter):
    x = symbols('x')
    f = lambdify(x, func_expr, modules=["numpy"])
    f_prime = lambdify(x, diff(func_expr, x), modules=["numpy"])
    f_double_prime = lambdify(x, diff(func_expr, x, 2), modules=["numpy"])

    iteraciones = []
    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_prime_x0 = f_prime(x0)
        f_double_prime_x0 = f_double_prime(x0)
        denominator = f_prime_x0 ** 2 - f_x0 * f_double_prime_x0
        if denominator == 0:
            return None, f"División por cero en x={x0}.", iteraciones
        x1 = x0 - (f_x0 * f_prime_x0) / denominator
        error = abs(x1 - x0)
        iteraciones.append({
            'No.': i,
            '(x0)': x0,
            '(x)': x1,
            'f(x0)': f_x0,
            'f´(x0)': f_prime_x0,
            'f´´(x0)': f_double_prime_x0,
            'Error': error
        })

        if error < tol:
            break
        x0 = x1
    return x1, "Newton Raphson Modificado", iteraciones
