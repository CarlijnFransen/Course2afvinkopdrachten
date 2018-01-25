#afvink 6
#door: Carlijn Fransen
import time
import sys
import re

def main():
    start_time = time.time()
    for i in range(1,11):
        print('iteratief: ',fib(i))
    print('--- %s secondes ---' % (time.time() - start_time))

    start_time1 = time.time()

    for i in range(1,11):
        print('recursie: ',recfib(i))
    print('--- %s secondes ---' % (time.time() - start_time1))

    is_dna()
    is_dna2()
    start_time2 = time.time()
    is_dna3
    print('--- %s secondes ---' % (time.time() - start_time2))    
def fib(n):
    start_time = time.time()
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b

    return a

def recfib(n):
    start_time = time.time()
   
    if n <= 1:

        return n
    else:
        return(recfib(n-1) + recfib(n-2))
def is_dna():
    start_time =  time.time()
    dna = 'test3.fa'
    result =  True
    for line in open(dna):
        if '>' not in line:
            line = line.replace('\n','')
    
            x = re.search("[^ATCGN]", dna)
            if x:
                result = True
    if result is True:
        print('Uw sequentie is DNA')
    else:
        print('Uw sequentie is geen DNA')
    print('--- %s secondes ---' % (time.time() - start_time))

def is_dna2():
    start_time = time.time()
    dna= 'test3.fa'
    result =  True
    for line in open(dna):
            if '>' not in line:
                line = line.replace('\n','')
                for x in line:
                    if x != 'A' and x != 'T' and x != 'C' and x != 'G' and x != 'N':
                        result = False
    if result==False:
        print('Uw sequentie is geen DNA')
    else:
        print(' Uw sequentie is DNA')
    print('--- %s secondes ---' % (time.time() - start_time))

def is_dna3():
    start_time =  time.time()
    sys.setrecursionlimit(1500)
    sequence = 'test3.fa'
    if len(sequence) <=1000:
        if len(sequence) == 0:
            return True
        else:
            if sequence [0] in 'ATCG':
                return is_dna_recursive(sequence[1:])
            else:
                return False
    else:
        sub_sequence = sequence [:1000]
        sentinel = sub_is_dna_recursive(sub_sequence)
        if sentinel is False:
            return False
        else:
            return is_dna_recursive(sequence[1000:1])

        
def is_dna_recursive():
    if len(sub_sequence):
        return True
    if sub_sequence[0] in 'ATCG':
        return sub_is_dna_recursive(sub_sequence[1:])
    else:
        return False

    
main()
