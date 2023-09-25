def degree_of_number(number, degree):
    if degree <= 1:
        return number

    return number * degree_of_number(number, degree - 1)

print(degree_of_number(3, 4))

# degree_of_number(3, 4) -> 3 * degree_of_number(3, 3) => 81
# degree_of_number(3, 3) -> 3 * degree_of_number(3, 2) => 27
# degree_of_number(3, 2) -> 3 * degree_of_number(3, 1) => 9
# degree_of_number(3, 1) => 3



user_number_of_stars = int(input("Введите количество звезд "))
def show_stars(number_of_stars):
    if number_of_stars > 0:
        print("* ", end = "")
        show_stars(number_of_stars - 1)


show_stars(user_number_of_stars)


# n > 0  show_stars(5) -> print("* ") n - 1
# n > 0  show_stars(4) -> print("* ") n - 1
# n > 0  show_stars(3) -> print("* ") n - 1
# n > 0  show_stars(2) -> print("* ") n - 1
# n > 0  show_stars(1) -> print("* ") n - 1
# n == 0 end


print()


num_1_for_interval = int(input("Введите начало интервала "))
num_2_for_interval = int(input("Введите конец "))

def sum_of_interval_nums(num_a, num_b):
     if num_a < num_b:
         num_a += sum_of_interval_nums(num_a + 1, num_b)

     return num_a

print(sum_of_interval_nums(num_1_for_interval, num_2_for_interval))

# sum_of_interval_nums(2, 6) -> 2 + sum_of_interval_nums(3, 6) => 20     |    ^
# sum_of_interval_nums(3, 6) -> 3 + sum_of_interval_nums(4, 6) => 18     |    |
# sum_of_interval_nums(4, 6) -> 4 + sum_of_interval_nums(5, 6) => 15     |    |
# sum_of_interval_nums(5, 6) => 5 + sum_of_interval_nums(6, 6) => 11     | -> |