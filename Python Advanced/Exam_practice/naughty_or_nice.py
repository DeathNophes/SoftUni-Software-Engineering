def naughty_or_nice_list(kids_list, *args, **kwargs):
    result = ""
    my_list = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for element in args:
        num, kid_type = element.split('-')
        num_count = 0

        for pair in kids_list:
            if str(pair[0]) == num:
                num_count += 1
                if num_count > 1:
                    break

        if num_count == 1:
            for pair in kids_list:
                if str(pair[0]) == num:
                    my_list[kid_type].append(pair[1])
                    index = kids_list.index(pair)
                    del kids_list[index]
                    break

    for kid_name, kid_type in kwargs.items():
        name_count = 0

        for pair in kids_list:
            if kid_name == pair[1]:
                name_count += 1
                if name_count > 1:
                    break

        if name_count == 1:
            for pair in kids_list:
                if kid_name == pair[1]:
                    my_list[kid_type].append(pair[1])
                    index = kids_list.index(pair)
                    del kids_list[index]
                    break

    for el in kids_list:
        my_list["Not found"].append(el[1])

    for kids_type, names_list in my_list.items():
        if names_list:
            result += f"{kids_type}: {', '.join(names_list)}\n"

    return result
