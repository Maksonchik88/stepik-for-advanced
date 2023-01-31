def info_kwargs(**kwargs):
    data = sorted(kwargs.items())
    for elem in data:
        print(elem[0], ':', f' {elem[1]}', sep='')



info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
