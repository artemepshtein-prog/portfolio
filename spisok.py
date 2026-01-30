


calculate_mean = [1, 3, 5, 4, 5, 5]
calculate_mean_2 = [4, 4, 3]

def calculate():
    all_grades = calculate_mean + calculate_mean_2
    mean = sum(all_grades) / len(all_grades)
    print(mean)

calculate()