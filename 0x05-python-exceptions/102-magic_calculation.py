#!/usr/bin/python3
def magic_calculation(a, b):
    # Initialize result to 0
    result = 0
    
    # Loop from 1 to 3 (inclusive)
    for i in range(1, 4):
        try:
            # Check if i is greater than a
            if i > a:
                # If true, raise an exception with the message 'Too far'
                raise Exception('Too far')
            
            # If no exception, perform the following calculations
            result += (a ** b) / i
        except Exception:
            # If an exception is caught, perform the following calculations
            result += a + b
    
    # Return the final result after the loop
    return result

