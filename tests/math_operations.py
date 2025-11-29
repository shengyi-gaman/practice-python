"""
Advanced mathematical operations module.
Provides utility functions for complex mathematical calculations.
"""

import math
from typing import Union, List


def power(base: Union[int, float], exponent: Union[int, float]) -> float:
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        The result of base^exponent
    """
    return base ** exponent


def square_root(number: Union[int, float]) -> float:
    """
    Calculate the square root of a number.
    
    Args:
        number: The number to find the square root of
        
    Returns:
        The square root of the number
        
    Raises:
        ValueError: If number is negative
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.
    
    Args:
        n: The number to calculate factorial for
        
    Returns:
        The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_prime(number: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        number: The number to check
        
    Returns:
        True if the number is prime, False otherwise
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def calculate_circle_area(radius: Union[int, float]) -> float:
    """
    Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle
        
    Returns:
        The area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def calculate_circle_circumference(radius: Union[int, float]) -> float:
    """
    Calculate the circumference of a circle.
    
    Args:
        radius: The radius of the circle
        
    Returns:
        The circumference of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius

def add(a: int, b: int) -> int:
    """
    Return the sum of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b
