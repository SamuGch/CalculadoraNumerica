from sympy import diff, symbols, lambdify


def newton_method(func_expr, x0, tol, max_iter):
    x = symbols('x')
    f = lambdify(x, func_expr, modules=["numpy"])
    f_prime = lambdify(x, diff(func_expr, x), modules=["numpy"])

    iteraciones = []
    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_prime_x0 = f_prime(x0)
        if f_prime_x0 == 0:
            return None, f"Derrivada nula en x={x0}.", iteraciones
        x1 = x0 - f_x0 / f_prime_x0
        error = abs(x1 - x0)
        iteraciones.append({
            'No.': i,
            '(x0)': x0,
            '(x)': x1,
            'f(x0)': f_x0,
            'f´(x0)': f_prime_x0,
            'Error': error
        })
        if error < tol:
            break
        x0 = x1
    return x1, "Newton Raphson", iteraciones
