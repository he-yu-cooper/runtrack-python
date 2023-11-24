def calculate_distance(steps, step_height):
    # Convert step height from cm to m
    step_height_m = step_height / 100

    # Calculate the distance the keeper walks every day (down and up once)
    daily_distance = 2 * steps * step_height_m

    # Calculate the distance the keeper walks every week (there are 7 days in a week)
    weekly_distance = 7 * daily_distance

    return weekly_distance

# Call the function
steps = 10
step_height = 20
print(f'For {steps} steps of {step_height} cm, the keeper walks {calculate_distance(steps, step_height):.2f} m per week.')
