from error_handling import handle_error
from error_handling import handle_error_context
from functional import BoundedMeta
from functional import BoundedBase
from functional import smart_function
from random import random


@handle_error(re_raise=True, tries=3, delay=0.5, backoff=2)
def some_function ():
    t=random()
    print(t)
    if  t<0.75:
        x=1/0


class C(metaclass=BoundedMeta, max_instance_count=2):
     pass


class D(BoundedBase):
    @classmethod
    def get_max_instance_count(cls):
        return 1


if __name__ == '__main__':
    # some_function()
    # with handle_error_context(log_traceback=True, exc_type=ValueError):
    #     raise ValueError()
    print(1)

    c1 = C()
    c2 = C()
    try:
        c3 = C()
    except TypeError:
        print('everything works fine!')
    else:
        print('something goes wrong!')

    d1 = D()

    try:
        d2 = D()
    except TypeError:
        print('everything works fine!')
    else:
        print('something goes wrong!')

    for real_call_count in range(1, 5):
        assert smart_function() == real_call_count
