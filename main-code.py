from vle import antoine_pressure, bubble_point_pressure, vapor_composition

# Temperature (Celsius)
T = 78.0

# Antoine constants
# Ethanol
A1 = 8.20417
B1 = 1642.89
C1 = 230.3

# Water
A2 = 8.07131
B2 = 1730.63
C2 = 233.426

# Liquid phase composition
x1 = 0.5  # Ethanol
x2 = 0.5  # Water

# Saturation pressures
Psat1 = antoine_pressure(A1, B1, C1, T)
Psat2 = antoine_pressure(A2, B2, C2, T)

# Bubble point pressure
P = bubble_point_pressure(x1, x2, Psat1, Psat2)

# Vapor phase composition
y1 = vapor_composition(x1, Psat1, P)
y2 = vapor_composition(x2, Psat2, P)

# Output
print("VLE CALCULATION RESULTS")
print("-----------------------")
print("Temperature:", T, "°C")
print("Bubble point pressure:", round(P, 2), "mmHg")
print()
print("Vapor phase composition:")
print("y1 (Ethanol) =", round(y1, 3))
print("y2 (Water)  =", round(y2, 3))
