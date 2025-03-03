# asgmt-1-programming-design-2025

> Programming Design 2025

## 01. Define a function `is_return_necessary_for_assignments()` which answers whether a `return` statement is necessary or not in our assignments.

```python
def is_return_necessary_for_assignments() -> bool:
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `calculate_movie_minutes()` which returns the time of a movie in minutes given hours and minutes.

```python
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
    
    ### END SOLUTION
```

## 03. Define a function named `calculate_bmi()` which calculates BMI given heights in centimeters and weights in kilograms.

$$
\text{BMI} = \frac{\text{weight}_{\text{kg}}}{\text{height}_{\text{m}}^2}
$$

```python
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
    
    ### END SOLUTION
```

## 04. Define a function `format_number_of_assignments_exams()` which returns the number of assignments and exams for this course.

```python
def format_number_of_assignments_exams(n_assignments: int, n_exams: int) -> str:
    """
    >>> format_number_of_assignments_exams(6, 2)
    '6 assignments 2 examinations'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `repeat_n_times()` which returns a concatenated `str` given an integer `n`.

```python
def repeat_n_times(str_to_repeat: str, n: int) -> str:
    """
    >>> repeat_n_times("Important!", 3)
    'Important!Important!Important!'
    >>> repeat_n_times("Go!", 3)
    'Go!Go!Go!'
    >>> repeat_n_times("Awesome!", 2)
    'Awesome!Awesome!'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `format_temperature_degrees()` which returns Fahrenheit degrees in text format given Celsius degrees.

$$
\text{Fahrenheit}^{\circ} \text{F} = \text{Celsius}^{\circ} \text{C} \times \frac{9}{5} + 32
$$

```python
def format_temperature_degrees(celsius: int) -> str:
    """
    >>> format_temperature_degrees(0)
    '0 Degrees Celsius = 32.0 Degrees Fahrenheit'
    >>> format_temperature_degrees(100)
    '100 Degrees Celsius = 212.0 Degrees Fahrenheit'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `format_integer_with_dollar_sign_and_commas()` which returns a comma format with dollar sign given an integer.

```python
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
    
    ### END SOLUTION
```

## 08. Define a function `is_positive()` which returns whether input is a positive integer or not.

```python
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
    
    ### END SOLUTION
```

## 09. Define a function `is_even()` which returns whether input is an even number or not.

```python
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
    
    ### END SOLUTION
```

## 10. Define a function `are_vowels_contained()` which returns whether input text contains one of the vowels: a, e, i, o, u.

```python
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
    
    ### END SOLUTION
```