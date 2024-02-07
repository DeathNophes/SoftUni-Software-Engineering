def team_lineup(*args):
    result = ""
    some_dict = {}
    for name, country in args:
        if country not in some_dict:
            some_dict[country] = []
        some_dict[country].append(name)

    sorted_dict = sorted(some_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for country, footballers in sorted_dict:
        result += f"{country}:\n"
        for player in footballers:
            result += f"  -{player}\n"

    return result
