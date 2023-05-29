from Linear import Linear
from fractions import Fraction

def get_minimum_degree(delta, e=None):
    if delta <= 1:
        raise Exception
    (f"delta needs to be larger than one, but was {delta}")
    a = delta / (delta - 1)
    b = 1
    if e:
        return a * e + b
    else:
        return Linear(a, b)

def get_infinum_locality(delta, e=None):
    if delta <= 1:
        raise Exception
    (f"delta needs to be larger than one, but was {delta}")
    a = delta / (delta - 1) + 2
    b = 2
    if e:
        return a * e + b
    else:
        return Linear(a, b)

def get_latex_table_row(delta):
    line = f"${float(delta)}$"
    line += " & "
    line += "$ \\geq " + str(get_minimum_degree(delta)) + " $"
    line += " & "
    line += "$ > " + str(get_infinum_locality(delta)) + " $"
    line +=" \\\\"
    return line

for a in list(range(11, 31, 1)) + [35, 40, 45, 50]:
    delta = Fraction(a, 10)
    print(get_latex_table_row(delta))
