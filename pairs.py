""" finds pairs of integers from a list that 
sum to a given value. """
def findPairs(numbers, sum):
  pairs = []
  numbers.sort() # Timsort complexity: nlogn
  i = 0
  j = len(numbers) - 1
  while (i < j): # complexity: n
    x = sum - numbers[i]
    if (numbers[j] == x):
      pairs.append(f'{numbers[i]}, {numbers[j]}')
      i+=1
      j-=1
    elif (numbers[j] > x):
      j-=1
    else:
      i+=1
  return pairs


def main():
  print('Digit the list of numbers (comma separated):')
  inputNumbers = input()
  print('Digit the target sum:')
  inputSum = input()

  try:
    numbers = [int(n) for n in inputNumbers.split(',')]
    sum = int(inputSum)
  except:
    print('Invalid input')
    return

  # final complexity: nlogn
  print(findPairs(numbers, sum))


if __name__ == '__main__':
  main()