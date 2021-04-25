from special_sum import calculate_special_sum
from diff_pairs import get_pairs_count
from primes import get_primes
from stochastic import StochasticSet

from hist import distribute
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(calculate_special_sum(3))
    # # print(get_pairs_count((5, 4, 3, 2, 1, 2, 4, 3, 5), 1))
    # print(get_primes(11))
    # distribute([1.25, 1, 2, 1.75], 2)
    p = StochasticSet()
    p.insert(55)
    p.insert(67)
    p.insert(33)
    p.insert(29)
    p.insert(1)
    p.insert(108)
    p.remove(8921)
    # p.remove(108)
    # p.remove(29)
    p.remove(33)
    p.remove(1)
    p.remove(55)
    print(p.get())
    p.remove(67)
    print(p.get())
