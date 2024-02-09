def age_assignment(*names, **kwargs):
    result = []
    for name in sorted(names):
        result.append(f"{name} is {kwargs[name[0]]} years old.")
    
    return "\n".join(result)
