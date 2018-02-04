from learn_and_try.python_book_src.chapter_09.car import Car
from learn_and_try.python_book_src.chapter_09.electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2015)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2015)
print(my_tesla.get_descriptive_name())
