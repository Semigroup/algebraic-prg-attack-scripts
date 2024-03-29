import math

# computes tables for multivariate non-local PRGs of fixed degree and fixed security bits



def get_min_seed_size(degree, sec_bits, e):
    """
    returns a number min_seed_size s.t. a PRG F : {0,1}^n --> {0,1}^{n^{1+e}}
    of d >= degree needs at least seeds of size n >= min_seed_size
    to have sec_bits many security bits
    (assuming that the fastest attack needs 2^(n^(1-e/(d-1))) steps)
    """
    return math.ceil(sec_bits**((degree - 1) / (degree - 1 - e)))

def get_table_row_latex(degree, sec_bits, e):
    min_seed_size = get_min_seed_size(degree, sec_bits, e)
    line = f"${float(e)}$"
    line += " & "
    line += from_bits_to_bytes(min_seed_size)
    line +=" \\\\"
    return line

def get_table_row_markdown(degree, sec_bits, e):
    min_seed_size = get_min_seed_size(degree, sec_bits, e)
    m = math.floor(pow(min_seed_size, 1 + e))
    line = "| "
    line += f"${float(e)}$"
    line += " | "
    line += from_bits_to_bytes(min_seed_size)
    line +=" | "
    line += from_bits_to_bytes(m)
    line +=" | "
    return line

def from_bits_to_bytes(number_bits):
    if number_bits < 8:
        return f"{number_bits}b"
    else:
        n = math.ceil(number_bits / 8)
    
    magnitudes =['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']
    for m in magnitudes:
        if n < 1024:
            return f"{n:g} " + m
        n /= 1024.0
    n *= 1024.0
    return f"{n:g} EB"

# n = 1
# for i in range(80):
#     print(from_bits_to_bytes(n))
#     n*=2

sec_bits = 128
degree = 3

for e in list(range(1, 90)):
    print(get_table_row_markdown(degree, sec_bits, e/100.0))