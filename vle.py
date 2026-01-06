import math

def antoine_pressure(A, B, C, T):
    """
    Antoine equation
    Psat in mmHg
    T in Celsius
    """
    Psat = 10 ** (A - (B / (T + C)))
    return Psat


def bubble_point_pressure(x1, x2, Psat1, Psat2):
    """
    Raoult's law for bubble point pressure
    """
    P = x1 * Psat1 + x2 * Psat2
    return P


def vapor_composition(x, Psat, P):
    """
    Vapor phase mole fraction
    """
    y = (x * Psat) / P
    return y

