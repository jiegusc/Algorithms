import sympy
sympy.init_printing()

x_pos, x_vel, x_alt = sympy.symbols('x_pos, x_vel x_alt')

H = sympy.Matrix([sympy.sqrt(x_pos**2 + x_alt**2)])

state = sympy.Matrix([x_pos, x_vel, x_alt])
print(H.jacobian(state))

from sympy import Matrix
sympy.init_printing(use_latex='mathjax')
w_vel, w_alt, dt = sympy.symbols('w_vel w_alt \Delta{t}')
w = Matrix([[0, w_vel, w_alt]]).T
phi = Matrix([[1, dt, 0], [0, 1, 0], [0,0,1]])

q = w*w.T

print(sympy.integrate(phi*q*phi.T, (dt, 0, dt)))