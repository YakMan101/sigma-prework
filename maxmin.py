import random


def find_max_min(array):
  if not array:
    return ("Array is empty")

  max = min = array[0]

  for i in range(1, len(array)):
    if array[i] > max:
      max = array[i]
    elif array[i] < min:
      min = array[i]
    else:
      continue

  return (f'min: {min}, max: {max}')


if __name__ == '__main__':
  random_array = random.sample(range(-50, 50), random.randint(0, 25))
  print(random_array)
  print(find_max_min(random_array))
