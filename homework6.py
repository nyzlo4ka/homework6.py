my_dict = {"Petrov": 1024, "Ivanov": 1044, "Sidorov": 2047, "Zaicev": 7745}
print("Parking:", my_dict)
print("Test:", my_dict["Ivanov"], ",", my_dict.get("Savin"))
my_dict.update({"Koshkina": 4532,
                "Demin": 4763})
Delite = my_dict.pop("Sidorov")
print("Free parking:", Delite)
print("Parking new:", my_dict)

my_set = {5, 6, 9.8, 7, 5, 7, 9.8, True, 6, 3, "2", 6, False, 5, 9.8}
print(my_set)
my_set.update([555, "All"])
my_set.discard(False)
print(my_set)
