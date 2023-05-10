def f(x):
    return x**3 + x + 16

def df(x):
    return 3*x**2 + 1
def bisection(a, b, tol):
    if f(a)*f(b) > 0:
        print("No hay raíz en el intervalo dado")
        return None
    else:
        iter_count = 0
        while (b - a)/2.0 > tol:
            iter_count += 1
            c = (a + b)/2.0
            if f(c) == 0:
                print(f"Convergencia alcanzada después de {iter_count} iteraciones.")
                return c
            elif f(a)*f(c) < 0:
                b = c
            else:
                a = c
        print(f"Convergencia alcanzada después de {iter_count} iteraciones.")
        return (a + b)/2.0
def secant(x0, x1, tol):
    iter_count = 0
    while abs(x1 - x0) > tol:
        iter_count += 1
        x_temp = x1 - ((f(x1)*(x1 - x0)) / (f(x1) - f(x0)))
        x0, x1 = x1, x_temp
    print(f"Convergencia alcanzada después de {iter_count} iteraciones.")
    return x1
def newton_raphson(x0, tol):
    iter_count = 0
    while abs(f(x0)) > tol:
        iter_count += 1
        x0 = x0 - f(x0)/df(x0)
    print(f"Convergencia alcanzada después de {iter_count} iteraciones.")
    return x0
print("Método de la bisección:", bisection(-10, 10, 1e-6))
print("Método de la secante:", secant(-10, 10, 1e-6))
print("Método de Newton-Raphson:", newton_raphson(-10, 1e-6))
