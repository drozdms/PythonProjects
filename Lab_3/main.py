from iter_helpers import transpose
from iter_helpers import scalar_product
from utils import profile
from utils import timer
from linked_list import Node
from linked_list import flatten_linked_list
from os import stat
from os import listdir
from utils import calculate_stats


@profile
def some_function():
    return sum(range(100000000))


if __name__ == '__main__':
    expected = [[1, 2], [-1, 3]]
    actual = transpose([[1, -1], [2, 3]])
    assert expected == list(map(list, actual))
    print(int('1'))
    expected = None
    actual = scalar_product([1, '2', '3b', 4], [-1, 1, 2, -2])
    print(list(map(list, zip([1, 2, 3, 4], [-1, 1, 2, -2]))))
    assert expected == actual

    actual = scalar_product([1, 'xyz'], [-1, 1])
    assert actual is None

    result = some_function()
    #
    # with timer():
    #      print(sum(range(100000000)))

    r3 = Node(3, Node(Node(Node(19, Node(312312)), Node(25)), Node(Node(12, Node(55)))))
    r3_flattenned = flatten_linked_list(r3)  # 3 -> 19 -> 25 -> 12 -> None
    r3_expected_flattenned_collection = [3, 19, 312312, 25, 12, 55]
    print(r3_flattenned)
    assert r3_expected_flattenned_collection == list(r3_flattenned)

    stats = calculate_stats('/Users/macos/Movies')
    #print(stat('/Users/macos/Dropbox/University/МО/Books_MO.zip'))
    print(stats.total_size)
    print(stats.total_files)
