from classs import Hero, Hero_super
# импортировали крч
b = Hero("Hulk", "strongest") # на это можно внимание не обращять
c = Hero_super("Spiderman", "blasters")
# а это для вывода нашего  магического метода
print(c.__str__()) # это сам вывод

