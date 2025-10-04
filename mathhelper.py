# math_helper.py
# A modular, student-friendly math support tool for advanced topics
# Designed for educational use and GitHub readability

import sympy as sp
import numpy as np
import math
from sympy.parsing.sympy_parser import parse_expr

class MathHelper:
    def __init__(self):
        self.intro_message()

    def intro_message(self):
        print("📘 Welcome to Math Helper!")
        print("Type 'exit' to quit. You can ask about calculus, algebra, trig, or custom expressions.")

    def simplify_expression(self, expr):
        try:
            parsed = parse_expr(expr)
            simplified = sp.simplify(parsed)
            return f"Simplified: {simplified}"
        except Exception as e:
            return f"Error simplifying expression: {e}"

    def solve_equation(self, equation):
        try:
            lhs, rhs = equation.split('=')
            lhs_expr = parse_expr(lhs)
            rhs_expr = parse_expr(rhs)
            solution = sp.solve(lhs_expr - rhs_expr)
            return f"Solution: {solution}"
        except Exception as e:
            return f"Error solving equation: {e}"

    def derivative(self, expr, var='x'):
        try:
            parsed = parse_expr(expr)
            derivative = sp.diff(parsed, sp.Symbol(var))
            return f"Derivative: {derivative}"
        except Exception as e:
            return f"Error computing derivative: {e}"

    def integral(self, expr, var='x'):
        try:
            parsed = parse_expr(expr)
            integral = sp.integrate(parsed, sp.Symbol(var))
            return f"Integral: {integral} + C"
        except Exception as e:
            return f"Error computing integral: {e}"

    def evaluate(self, expr):
        try:
            parsed = parse_expr(expr)
            evaluated = parsed.evalf()
            return f"Evaluated: {evaluated}"
        except Exception as e:
            return f"Error evaluating expression: {e}"

    def run(self):
        while True:
            user_input = input("\n🔢 Enter your math query: ").strip()
            if user_input.lower() == 'exit':
                print("👋 Goodbye!")
                break
            elif 'solve' in user_input:
                equation = user_input.replace('solve', '').strip()
                print(self.solve_equation(equation))
            elif 'simplify' in user_input:
                expr = user_input.replace('simplify', '').strip()
                print(self.simplify_expression(expr))
            elif 'derivative' in user_input:
                expr = user_input.replace('derivative', '').strip()
                print(self.derivative(expr))
            elif 'integral' in user_input:
                expr = user_input.replace('integral', '').strip()
                print(self.integral(expr))
            elif 'evaluate' in user_input:
                expr = user_input.replace('evaluate', '').strip()
                print(self.evaluate(expr))
            else:
                print("⚠️ Please specify an action: solve, simplify, derivative, integral, or evaluate.")

if __name__ == "__main__":
    helper = MathHelper()
    helper.run()
