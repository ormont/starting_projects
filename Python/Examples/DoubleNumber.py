"""
Created on Sun Mar 29 12:43:43 2020
@author: morozco
"""

# ----------------------------------------------------------------------
def DoubleNumber(n):
    return 2*n

# ----------------------------------------------------------------------
def main():
    x = float(input("Enter a number x: "))
    print("2 * x =", DoubleNumber(x))
    
# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()