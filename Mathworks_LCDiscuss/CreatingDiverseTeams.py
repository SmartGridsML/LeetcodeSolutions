#Find number of ways to select a diverse team of 3 people
# Diverse - at least ione FE and at least one back end

def numberofDiverseTEams(f , b) -> int:
    if f == 0 or b == 0:
        return 0
    else: return ((f * b * (f + b -2))/2)
    
