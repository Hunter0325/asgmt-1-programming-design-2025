def is_return_necessary_for_assignments() -> bool:
    ### BEGIN SOLUTION
    return True
    ### END SOLUTION

def calculate_movie_minutes(hours: int, mins: int) -> int:
    """
    >>> calculate_movie_minutes(2, 22) # The Shawshank Redemption
    142
    >>> calculate_movie_minutes(2, 55) # The Godfather
    175
    >>> calculate_movie_minutes(2, 32) # The Dark Knight
    152
    """
    ### BEGIN SOLUTION
    return hours * 60 + mins
    ### END SOLUTION

def calculate_bmi(height: int, weight: int) -> float:
    """
    >>> calculate_bmi(216, 147) # Shaquille O'Neal in his prime
    31.507201646090532
    >>> calculate_bmi(206, 113) # LeBron James
    26.628334433028563
    >>> calculate_bmi(211, 110) # Giannis Antetokounmpo
    24.70744143213315
    """
    ### BEGIN SOLUTION
    return weight / (height*0.01)**2
    ### END SOLUTION

def format_number_of_assignments_exams(n_assignments: int, n_exams: int) -> str:
    """
    >>> format_number_of_assignments_exams(6, 2)
    '6 assignments 2 examinations'
    """
    ### BEGIN SOLUTION
    return f"{n_assignments} assignments {n_exams} examinations"
    ### END SOLUTION

def repeat_n_times(str_to_repeat: str, n: int) -> str:
    """
    >>> repeat_n_times("Important!", 3)
    'Important!Important!Important!'
    >>> repeat_n_times("Go!", 3)
    'Go!Go!Go!'
    >>> repeat_n_times("Awesome!", 2)
    'Awesome!'
    """
    ### BEGIN SOLUTION
    return str_to_repeat * n
    ### END SOLUTION

def format_temperature_degrees(celsius: int) -> str:
    """
    >>> format_temperature_degrees(0)
    '0 Degrees Celsius = 32.0 Degrees Fahrenheit'
    >>> format_temperature_degrees(100)
    '100 Degrees Celsius = 212.0 Degrees Fahrenheit'
    """
    ### BEGIN SOLUTION
    fah = celsius * 9/5 + 32
    return f"{celsius} Degrees Celsius = {fah} Degrees Fahrenheit"
    ### END SOLUTION

def format_integer_with_dollar_sign_and_commas(x: int) -> str:
    """
    >>> format_integer_with_dollar_sign_and_commas(1000)
    '$1,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000)
    '$1,000,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000000)
    '$1,000,000,000'
    """
    ### BEGIN SOLUTION
    return f"${x:,}"
    ### END SOLUTION

def is_positive(x: int) -> bool:
    """
    >>> is_positive(-1)
    False
    >>> is_positive(0)
    False
    >>> is_positive(1)
    True
    """
    ### BEGIN SOLUTION
    return x > 0
    ### END SOLUTION

def is_even(x: int) -> bool:
    """
    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(4)
    True
    """
    ### BEGIN SOLUTION
    return x % 2 == 0
    ### END SOLUTION

def are_vowels_contained(x: str) -> bool:
    """
    >>> are_vowels_contained('pythn')
    False
    >>> are_vowels_contained('ncnd')
    False
    >>> are_vowels_contained('rtclt')
    False
    >>> are_vowels_contained('python')
    True
    >>> are_vowels_contained('anaconda')
    True
    >>> are_vowels_contained('reticulate')
    True
    """
    ### BEGIN SOLUTION
    return ('a' in x) or ('e' in x) or ('i' in x) or ('o' in x) or ('u' in x)
    ### END SOLUTION