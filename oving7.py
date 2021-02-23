import string
from pathlib import Path


def make_words_list(path):
    word_array = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word = word.translate(str.maketrans('', '', string.punctuation))
                word = word.lower().strip()
                if len(word) != 0:
                    word_array.append(word)
    return word_array


'''Using quicksort. In this case the algorithm needs to be robust to repeated elements, using Dijkstras 'Dutch national 
    flag problem' solution.'''
def quick_sort_length(arr, start, end):
    if end <= start:
        return

    left, right = quick_sort_helper_length(arr, start, end)

    quick_sort_length(arr, start, left - 1)
    quick_sort_length(arr, right + 1, end)


def quick_sort_helper_length(arr, start, end):
    left = start
    mid = start
    right = end

    pivot = arr[start]

    while mid <= right:
        compared = compare(len(arr[mid]), len(pivot))
        if compared == -1:
            swap(arr, mid, left)
            mid += 1
            left += 1
        elif compared == 0:
            mid += 1
        else:
            swap(arr, mid, right)
            right -= 1
    return left, right


'''Making the lexographic sort its own function, the only difference is the values it
 compares in the helper/partition function.'''
def quick_sort_lexographic(arr, start, end):
    if end <= start:
        return

    left, right = quick_sort_helper_lexographic(arr, start, end)

    quick_sort_lexographic(arr, start, left - 1)
    quick_sort_lexographic(arr, right + 1, end)


def quick_sort_helper_lexographic(arr, start, end):
    left = start
    mid = start
    right = end

    pivot = arr[start]

    while mid <= right:
        compared = compare(arr[mid], pivot)  # this is the only difference between the functions
        if compared == -1:
            swap(arr, mid, left)
            mid += 1
            left += 1
        elif compared == 0:
            mid += 1
        else:
            swap(arr, mid, right)
            right -= 1
    return left, right


# Some helper functions:
def swap(arr, left, right):
    if arr[left] != arr[right]:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp


def compare(var1, var2):
    if var1 > var2:
        return 1
    elif var1 < var2:
        return -1
    else:
        return 0


if __name__ == '__main__':
    path = Path('testfile.txt')
    word_arr = make_words_list(path)

    quick_sort_lexographic(word_arr, 0, len(word_arr) - 1)  # sort alphabetically first
    quick_sort_length(word_arr, 0, len(word_arr) - 1)  # sorting by length should not affect the lexographic sort

    print(word_arr)
