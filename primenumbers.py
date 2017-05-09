"""Prime numbers module 
to print out numbers with an assyptotic analysis considering that any number of elements can be printed"""


from math import factorial

def primenumbers(n):
    """Function to generate prime numbers within given range."""

    prime_nos = [] # should return a list

    # numbers other th
    if n in (0, 1):
        return "Zero or One cannot be prime numbers."

    if n < 0:
        return "cannot takke in negative numbers"
    if n < 2:
        return "the smallest pprime number is two"

    # only integers taken as input
    if type(n) != int:
        return "Only integers are allowed."


    # considering that any number of prime numbers should be printed efficiently

    # both the for and while loops will do the same thing
    # the infinite while loop is more efficient compared to for 

    else:
        i=2
        while True:
            prime_nos = [i for i in range(2,n+1) if (factorial(i-1)+1)%i==0]

            return prime_nos       