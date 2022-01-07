#You have an N x M matrix, where 1 to N are rows and 1 to M are columns.

#Element at the intersection of i row and j column is equal to F(i +j), 
# where F(x)  is equal to the number of prime divisors of x.

#Determine the sum of all the elements of the matrix.

#Input

#The first line contains an integer T denoting the number of test cases.
#For each test case, the first line contains two space-separated integers N, M.
#Output

#For each test case, print the sum of all the elements of the matrix  in a new line.

# sample  input
#1
#3 3
# sample output
#10
# builtin prime factors module  in python


# function of sieve Of Eratosthenes
check_time = False
if check_time: from time import perf_counter
 
# used in old version
def sieveOfEratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    if n <= 2:
        return []
    sieve = list (range (3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]
 
# based on methodic of sieveofEratosthenes
def distinct_prime_counts (n):
    """ return the list of count of distinct prime factors for each n"""
    if n <= 2:
        return [0, 0]
    ctd = [0] * (n + 2)
    ctd [2::2] = [1] * ((n + 1) // 2)
    for i in range (3, n, 3): ctd [i] += 1
    f = 5
    while f < n:
        if not ctd [f]: 
            for i in range (f, n, f): ctd [i] += 1
        f2 = f + 2
        if not ctd [f2]:
            for i in range (f2, n, f2): ctd [i] += 1
        f += 6
    return ctd
 
# used in old version
def ct_divs (primes, cost):
    res = 0
    seen = set ()
    while cost > 1:
        if cost in primes:
            if cost not in seen: res += 1
            break
        for div in primes:
            if cost % div == 0:
                if div not in seen:
                    res += 1
                    seen.add (div)
                cost //= div
                break
    return res
 
def main ():
    
    if check_time: tim = perf_counter ()
    
    t = int (input ())
    nml = []
    mnmax = 0
    for t_ in range (t):
        n, m = map (int, input ().split ())
        if n > mnmax: mnmax = n
        if m > mnmax: mnmax = m
        nml.append ((n, m))
    if check_time: 
        print ("n, m read, max n, m in ", perf_counter () - tim)
        tim = perf_counter ()
    
    #primes = set (sieveOfEratosthenes (mnmax * 2))
    """if check_time: 
        print ("primes up to", mnmax * 2, "generated in", perf_counter () - tim)
        tim = perf_counter ()"""
    
    ctd = distinct_prime_counts (2 * mnmax + 1) [1:] # get list by shift of 1
    # to avoid +1 for millions of operations, when collecting total
 
    # old version of building list of count of prime factors:
    # (20 times slower !)
    #ctd = [0] * (2 * mnmax + 1)
    #for i in range (2 * mnmax + 1): ctd [i] = ct_divs (primes, i)
    #print (ctd)
    if check_time: 
        print ("count of prime divisors list generated in", perf_counter () - tim)
        tim1 = tim = perf_counter ()
    
    for n, m in nml:
        nm = n + m
        if n > m: n, m = m, n
        m_1 = m - 1; np1 = n + 1
        tot = 0
        for i in range (1, n):
            tot += i * ctd [i] + (np1 - i) * ctd [i + m_1]
        for i in range (n, m):
            tot += n * ctd [i]
        tot += ctd [n + m_1]
        if check_time:
            print (n, m, n + m, tot, perf_counter () - tim)
            tim = perf_counter ()
        else: print (tot)
    
    if check_time: print ("matrix processed in", perf_counter () - tim1)
 
if __name__ == "__main__": main ()



