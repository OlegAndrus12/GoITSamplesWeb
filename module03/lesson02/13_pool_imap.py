'''
Class is used to implement an iterator

Function is used to implement a generator.

Local Variables aren’t used here.                                         

All the local variables before the yield function are stored. 

Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.                                                               	Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop
Iterator uses iter() and next() functions 	Generator uses yield keyword
Every iterator is not a generator	Every generator is an iterator
'''

from multiprocessing import Pool

def worker(val):
    return val ** 2


if __name__ == '__main__':

    with Pool(2) as pool:
        r = pool.map(worker, range(10))
        print(r)

        iterator = pool.imap(worker, range(10))
        print(iterator)
        [print(el, end=" ") for el in iterator]
