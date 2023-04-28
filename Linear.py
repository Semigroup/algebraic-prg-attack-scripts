from fractions import Fraction


def fraction_to_latex(fraction):
    frac = fraction.as_integer_ratio()
    if(frac[1] == 1):
        return str(frac[0])
    else:
        return "{" + str(frac[0]) + "}/{" + str(frac[1]) + "}" 

class Linear():
    def __init__(self, coefficient, absolute) -> None:
        self.absolute = absolute
        self.coefficient = coefficient
    
    def __str__(self) -> str:
        result = fraction_to_latex(self.coefficient)
        result += " \\cdot e + "
        result += fraction_to_latex(self.absolute)
        return result
        
        