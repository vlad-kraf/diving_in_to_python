import functools
from collections import namedtuple
from collections import defaultdict

statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])


def collect_statistics(arg1):
    def real_decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):

            result = func(*args, **kwargs)

            if result[1] == args[1]:
                my_order = Order(result[0], result[1])
            else:
                my_order = Order(result[0], args[1]-result[1])

            arg1[args[0]].append(my_order)

            return result
        return wrapped
    return real_decorator


@collect_statistics(statistics)
def check_portions(food, count, recipes=recipes, store=store):
    # напишите вашу реализацию функции здесь
    if food in recipes:
        portions = min(store.get(k,0) // v for k, v in recipes.get(food).items())
    else:
        portions = 0
    return (0, portions,) if portions < count else (1, count,)

"""
Эталон:

from collections import namedtuple
from collections import defaultdict

statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])

def collect_statistics(statistics):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            food, count = args
            response_code, max_count = func(*args, **kwargs)
            portions = max_count if response_code else count - max_count
            statistics[food].append(Order(response_code, portions))
            return response_code, max_count
        return inner
    return decorator


def get_max_portions(food, recipes, store):
    portions = []
    for ingredient, count in recipes[food].items():
        portions.append(store.get(ingredient, 0) // count)
    return min(portions)


@collect_statistics(statistics)
def check_portions(food, count, recipes=recipes, store=store):
    max_portions = get_max_portions(food, recipes, store)
    if max_portions < count:
        return 0, max_portions
    return 1, count
"""