def safe_divide(numerator, denominator):
    try:
        num = float(numerator) #convert the numerator to float
        den = float(denominator) # convert the denominator to float
                
        if den == 0:
            return "Error: Cannot divide by zero."
        
        return f"Result: {num / den }"
    except ValueError:
        return "Error: Both inputs must be numeric."