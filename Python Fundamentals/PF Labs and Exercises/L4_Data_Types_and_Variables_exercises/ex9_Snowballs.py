number_of_snowballs = int(input())
highest_value_snowball = 0
highest_value_snowball_weight = 0
highest_value_snowball_time = 0
highest_value_snowball_quality = 0
for snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_to_hit_target = int(input())
    quality_of_snowball = int(input())
    value_of_snowball = (weight_of_snowball / time_to_hit_target) ** quality_of_snowball
    if value_of_snowball > highest_value_snowball:
        highest_value_snowball = value_of_snowball
        highest_value_snowball_weight = weight_of_snowball
        highest_value_snowball_time = time_to_hit_target
        highest_value_snowball_quality = quality_of_snowball
print(f"{highest_value_snowball_weight} : {highest_value_snowball_time} = "
      f"{highest_value_snowball:.0f} ({highest_value_snowball_quality})")
