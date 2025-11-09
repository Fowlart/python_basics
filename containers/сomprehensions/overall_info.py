# Comprehensions — це стислий і елегантний спосіб створювати нові колекції
# (list, set, dict) на основі існуючих ітерабельних об'єктів. Вони є дуже швидкими,
# оскільки оптимізовані на рівні C-імплементації Python.
import json

if __name__ == "__main__":

    the_list = [x * 2 for x in range(20)]
    print(the_list)

    the_set = {x % 3 for x in range(20)}
    print(the_set)

    the_dict = {x: x*x for x in range(6)}
    print(json.dumps(the_dict, indent=3))

    # `map`
    mapped_list = [str(el) for el in the_list]
    print(mapped_list)

    # `filter`
    mapped_list = [el for el in mapped_list if '2' in el]
    print(mapped_list)