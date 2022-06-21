def calculate_simple_interest(initial,interest,years):
    interest =  interest / 100
    current_inversion = initial
    for _ in range(years):
        current_inversion = current_inversion + (initial * interest)
    return current_inversion

def calculate_compound_interest(initial,interest,years):
    interest =  interest / 100
    current_inversion = initial
    for _ in range(years):
        current_inversion = current_inversion + (current_inversion * interest)
    return current_inversion

def calculate_compound_interest_plus_re_inversion(initial,monthly_inversion,years,interest):
    """
    This function calculates the compound interest of an initial inversion were there is a constant monthly reinversion

    initial: float -> your initial inversion
    monthly_inversion: float -> a monthly amount to increase the inversion
    years: int -> how many years your inversion is going to stay
    interest: what percentage of interest your inversion has
    """
    current_inversion = initial
    interest =  interest / 100
    for _ in range(years):
        current_inversion = current_inversion + (monthly_inversion * 12)
        current_inversion = current_inversion + (current_inversion * interest)
    return current_inversion

if __name__ == '__main__':
    res = calculate_compound_interest_plus_re_inversion(5000,5000,2,4)
    print(res)