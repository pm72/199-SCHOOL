number_of_floor = 5
number_of_home = 20
number_homes_on_floor = number_of_home // number_of_floor

home_number = int(input("Enter number of home [1..20]: "))
floor = (home_number + number_homes_on_floor - 1) // number_homes_on_floor

print(f"This home is on floor {floor}")
