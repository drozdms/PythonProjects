from time import sleep
from logging import exception
from contextlib import contextmanager


def handle_error(re_raise=True, log_traceback=True, exc_type=Exception, tries=1, backoff=1, delay=0):
    def wrapper(func):
        def inner(*args, **kwargs):
            re_raise_ = re_raise
            i = 1
            delay_ = delay
            foreign_raised = True
            attempting = True
            while True:
                try:
                    func(*args, **kwargs)
                except exc_type:
                    if log_traceback:  # printing log always -- even when not reraising
                        exception("Exception Raised")
                    foreign_raised = False
                    if i < tries:
                        break
                else:
                    foreign_raised = attempting = re_raise_ = False
                finally:
                    if foreign_raised:
                        raise Exception("Reraising an exception not of exc_type")
                    if attempting and i < tries:
                        delay_ *= backoff
                        sleep(delay_)
                        i += 1
                        continue
                    if re_raise_:
                        raise exc_type("Reraising caught exception")
                    break

        return inner

    return wrapper


@contextmanager
def handle_error_context(re_raise=True, log_traceback=True, exc_type=Exception):
    foreign_raised = True
    while True:
        try:
            yield
        except exc_type:
            if log_traceback:  # printing log always -- even when not reraising
                exception("Exception Raised")
            foreign_raised = False
        else:
            foreign_raised = re_raise = False
        finally:
            if foreign_raised:
                raise Exception("Reraising an exception not of exc_type")
            if re_raise:
                raise exc_type("Reraising caught exception")
            break
