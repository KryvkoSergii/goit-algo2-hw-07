# Cache management algorithms
## Task 1. Data Access Optimization Using LRU Cache

Implement a program to optimize processing of queries to an array of numbers using LRU cache.

### Specifications

1. Given an array of size `N`, consisting of positive integers `(1 ≤ N ≤ 100_000)`. It is necessary to process `Q` queries `(1 ≤ Q ≤ 50_000)` of the following type:

`Range(L, R)` — find the sum of elements in the range from index L to R inclusive.

`Update(index, value)` — replace the value of the element in the array at index index with a new value value.
2. Implement four functions for working with the array:

`range_sum_no_cache(array, L, R)`
The function should calculate the sum of the array elements in the range from `L` to `R` inclusive without using the cache. The result should be calculated anew for each query.

`update_no_cache(array, index, value)`
The function should update the value of the array element at the specified index without using the cache.

`range_sum_with_cache(array, L, R)`
The function should calculate the sum of the elements in the range from `L` to `R` inclusive, using the LRU cache. If the sum for this range has already been calculated before, it should be returned from the cache, otherwise the result is calculated and added to the cache.

`update_with_cache(array, index, value)`
The function should update the value of the array element at the specified index and remove all corresponding values ​​from the cache that have become irrelevant due to a change in the array.

3. To test the program, create an array of `100_000` elements filled with random numbers and generate `50_000` `Range` and `Update` queries in random order.

Example of a query list: `[('Range', 46943, 91428), ('Range', 5528, 29889), ('Update', 77043, 78), ...]`

4. Use an LRU cache of size `K = 1000` to store pre-computed results of Range queries. The cache should automatically remove the least recently used elements if its maximum size is reached.

5. Compare the execution times of the queries:
Without using the cache.
With using the LRU cache.
Print the results in terms of execution times for both approaches.

### Result 
```bash
length of array: 100000
number of scenarios: 50000
length of scenarios: 50000 generated
number of range scenarios: 25011, number of update scenarios: 24989
Execution time without caching: 95.13 seconds
Execution time with LRU cache: 97.86 seconds
```