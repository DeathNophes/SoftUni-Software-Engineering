def even_odd_filter(**numbers_sets):
    if 'odd' in numbers_sets:
        numbers_sets['odd'] = [n for n in numbers_sets['odd'] if n % 2 == 1]

    if 'even' in numbers_sets:
        numbers_sets['even'] = [n for n in numbers_sets['even'] if n % 2 == 0]

    return numbers_sets
