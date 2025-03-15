import timeit
from functools import lru_cache
from scenario_handler import ScenarioHandler, generate_random_array
from functools import reduce

def range_sum_no_cache(array, L, R):
    return reduce(lambda x, y: x + y, array[L:R+1], 0)

def update_no_cache(array, index, value):
    array[index] = value

@lru_cache(maxsize=1000)
def sum_with_cache(x, y):
    return x + y

def range_sum_with_cache(array, L, R):
    return reduce(lambda x, y: x + y, array[L:R+1], 0)

@lru_cache(maxsize=1000)
def range_sum_with_cached(L, R):
    return range_sum_with_cache(array, L, R)

def update_with_cache(array, index, value):
    array[index] = value
    sum_with_cache.cache_clear()

array = generate_random_array(100_000)
print(f"length of array: {len(array)}")
number_of_scenarios = 50_000
print(f"number of scenarios: {number_of_scenarios}")

scenarios = ScenarioHandler()
scenarios.generate_random_scenarios(len(array), number_of_scenarios)
range_count, update_count = scenarios.get_statistics()
print(f"number of range scenarios: {range_count}, number of update scenarios: {update_count}")

execution_time = timeit.timeit(lambda: scenarios.run_scenarios(array=array, range_sum=range_sum_no_cache, update=update_no_cache), number=3)
print(f"Execution time without caching: {execution_time:.2f} seconds")

execution_time = timeit.timeit(lambda: scenarios.run_scenarios(array=array, range_sum=range_sum_with_cached, update=update_with_cache, adhoc=True), number=3)
print(f"Execution time with LRU cache: {execution_time:.2f} seconds")