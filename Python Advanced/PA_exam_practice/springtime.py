def start_spring(**kwargs):
    result = ""
    nature_dict = {}

    for name, type in kwargs.items():
        if type not in nature_dict.keys():
            nature_dict[type] = []
        nature_dict[type].append(name)

    sorted_nature_dict = sorted(
        nature_dict.items(),
        key=lambda x: (-len(x[1]), x[0])
    )

    for curr_type, elements in sorted_nature_dict:
        result += f"{curr_type}:\n"
        for el in sorted(elements):
            result += f"-{el}\n"

    return result
