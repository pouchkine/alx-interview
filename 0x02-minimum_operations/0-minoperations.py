#!/usr/bin/python3
"""
Main file for t
"""
from math import sqrt


def is_prime(n):
    """
    determine if is nomber is prime number or not
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_list(n):
    """
    determine the list of prime number less/ equal than n
    """
    return [i for i in range(1, n) if is_prime(i)]


def primeFactor(n):
    """
    return the primes factors af a number in a list
    """
    limit = int(sqrt(n)) + 1
    primes = []
    if is_prime(n):
        return [n]
    for i in range(2, limit):
        while n % i == 0:
            primes.append(i)
            n = n/i
            n = int(n)
            if is_prime(n):
                primes.append(n)
                return primes
    return primes


def minOperations(n):
    """
    return the sum of primes factor of a number n
    """
    return sum(primeFactor(n))
