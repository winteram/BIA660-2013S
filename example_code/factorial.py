def myfactorial(n):
    """Expects an integer as input
    Returns the factorial of a number.
    """
    myfact = 1
    for i in range(n):
        myfact = myfact * (n - i)
    return myfact

def mychoose(n,k):
    """Returns the number of permutations for k draws from n items"""
    return myfactorial(n) / (myfactorial(k) * myfactorial(n - k))

if __name__ == "__main__":   
    
    print "The factorial for 6 = %d" % myfactorial(6)
    print "The number of permutations for 3 items chosen from a set of 10 = %d" % mychoose(10,3)
