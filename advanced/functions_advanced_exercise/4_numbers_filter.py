def even_odd_filter(**kwargs):
    even, odd = None, None
    nums_dict = {}
    if 'even' in kwargs.keys():
        even = kwargs['even']
    if 'odd' in kwargs.keys():
        odd = kwargs['odd']
    if even:
        even = list(filter(lambda x: x % 2 == 0, even))
        nums_dict['even'] = even
    if odd:
        odd = list(filter(lambda x: x % 2 == 1, odd))
        nums_dict['odd'] = odd

    sorted_dict = dict(sorted(nums_dict.items(), key=lambda x: -len(x[1])))

    return sorted_dict


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))



