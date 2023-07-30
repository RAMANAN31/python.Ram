

#1. `choice(seq)` - Random item from a list, tuple, or string.
```python
import random

my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)
print(random_item)  # Output: Randomly selected item from the list
```

#2. `randrange(start, stop, step)` - Randomly selected element from a range.
```python
import random

random_number = random.randrange(1, 10, 2)
print(random_number)  # Output: Randomly selected odd number between 1 and 10
```

#3. `random()` - Random float between 0 and 1.
```python
import random

random_float = random.random()
print(random_float)  # Output: Random float between 0 and 1
```

#4. `seed([x])` - Set the seed for generating random numbers.
```python
import random

random.seed(123)
random_number_1 = random.random()
random_number_2 = random.random()
print(random_number_1, random_number_2)  # Output: Same random numbers for the same seed
```

#5. `shuffle(lst)` - Randomly shuffle the items of a list in place.
```python
import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)  # Output: List with items shuffled randomly
```

#6. `uniform(x, y)` - Random float between x and y.
```python
import random

random_float = random.uniform(5, 10)
print(random_float)  # Output: Random float between 5 and 10
```

Note: The exact output for the random functions will vary on each run, as they generate random values.
