
class BoundedMeta(type):
    _instances = {}
    class_bound = {}

    def __call__(cls, *args, **kw):
        name = cls.__name__
        super(BoundedMeta, cls).__call__()
        if cls.class_bound[name] is None:
            return
        if cls.class_bound[name] > 0:
            if cls._instances[name] < cls.class_bound[name]:
                cls._instances[name] += 1
            else:
                raise TypeError("Cannot instantiate more objects")
        else:
            raise TypeError("Cannot instantiate more objects")
        return cls._instances[name]

    def __new__(mcs, name, bases, namespace, **kwargs):
        mcs.class_bound[name] = kwargs['max_instance_count'] if 'max_instance_count' in kwargs else None
        super(BoundedMeta, mcs).__new__(mcs, name, bases, namespace)
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, dict, **kwargs):
        super(BoundedMeta, cls).__init__(name, bases, dict)
        cls._instances[name] = 0


def call_counter(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@call_counter(counter=0)
def smart_function():
    smart_function.counter += 1
    return smart_function.counter


class BoundedBase(metaclass=BoundedMeta, max_instance_count=56):

    @classmethod
    def get_max_instance_count(cls):
        pass

    def __new__(cls, *args, **kwargs):
        cls.__class__.class_bound[cls.__name__] = cls.get_max_instance_count()
