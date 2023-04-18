def is_anagram(first_string, second_string):
    # Converter as strings de entrada para minúsculas
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Checa if a string is vazia
    if first_string == '' and second_string == '':
        return ('', '', False)

    # Classifica os caracteres das strings usando o Merge sort
    sorted_first_string = merge_sort(list(first_string))
    sorted_second_string = merge_sort(list(second_string))

    # Verifica se as strings ordenadas são iguais
    is_anagram = sorted_first_string == sorted_second_string

    return ("".join(sorted_first_string),
            "".join(sorted_second_string), is_anagram)


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)


def merge(lst1, lst2):
    result = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    result += lst1[i:]
    result += lst2[j:]

    return result
