# single-phase-half-wave-converter
import math

# Single Phase Half Wave Converter

Vm = float(input("Enter peak supply voltage Vm (V): "))
alpha = float(input("Enter firing angle alpha (in degrees): "))

# Average output voltage
Vdc = (Vm / (2 * math.pi)) * (1 + math.cos(math.radians(alpha)))

print("\nSingle Phase Half Wave Converter")
print("Peak voltage Vm =", Vm, "V")
print("Firing angle alpha =", alpha, "degrees")
print("Average output voltage Vdc =", round(Vdc, 2), "V")

Example

Input:

Enter peak supply voltage Vm (V): 230
Enter firing angle alpha (in degrees): 60


Output:

Single Phase Half Wave Converter
Peak voltage Vm = 230.0 V
Firing angle alpha = 60.0 degrees
Average output voltage Vdc = 91.83 V

Formula

For a single-phase half-wave controlled converter:

𝑉
𝑑
𝑐
=
𝑉
𝑚
2
𝜋
(
1
+
cos
⁡
𝛼
)

where:

Vm = peak AC supply voltage

α = firing angle of the SCR

Vdc = average DC output voltage
