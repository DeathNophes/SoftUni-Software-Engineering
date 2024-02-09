def math_operations(*numbers, **kwargs):
    keys = list(kwargs.keys())  # [a, s, d, m]

    for i in range(len(numbers)):
        key = keys[i % 4]   # Keys will always be 4 so we can only get 0, 1, 2, 3

        if key == 'a':
            kwargs[key] += numbers[i]
        elif key == 's':
            kwargs[key] -= numbers[i]
        elif key == 'd':
            if numbers[i] != 0:
                kwargs[key] /= numbers[i]
        elif key == 'm':
            kwargs[key] *= numbers[i]

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f"{k}: {v:.1f}" for k, v in result)
