recipes = {'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
           'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}}

store = {'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
         'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
         'Майонез': 50, 'Зелень': 20}
from collections import namedtuple
from collections import defaultdict

recipes = {'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
           'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}}

store = {'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
         'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
         'Майонез': 50, 'Зелень': 20}

food = 'Бутерброд с ветчиной'
count = 2

statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])
statistics[food].append(Order(7, 7))


def collect_statistics(arg1):
    def real_decorator(check_portions):
        def wrapper(*args, **kwargs):
            result = check_portions(food, count, recipes=recipes, store=store)

            # my_order = Order(result[0], result[1])

            statistics[food].append(Order(result[0], result[1]))

            print(result)

            return statistics

        wrapper.__name__ = check_portions.__name__
        return wrapper

    return real_decorator


@collect_statistics("arg1")
def check_portions(food, count, recipes=recipes, store=store):
    # напишите вашу реализацию функции здесь

    if food in recipes:
        portions = min(store.get(k, 0) // v for k, v in recipes.get(food).items())
    else:
        portions = 0
    return (0, portions,) if portions < count else (1, count,)


statistics = check_portions()

print(statistics)