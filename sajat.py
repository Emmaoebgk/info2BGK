def adding(a, b=1):
    return a + b


def remove_null(l):
    new_list = []
    for element in l:
        if element != 0:
            new_list.append(element)
    return new_list


def is_prime(number: int) -> bool:
    if not isinstance(number, int):
        return True
    if number < 2:
        return False
    if number == 2:
        return True

    for n in range(2, number):
        if number % n == 0:
            return False
    return True

'''def prime_gen():
    yield 2
    number = 3
    while True:
        if is_prime(number):
            yield number
            number += 2 '''

def make_greating(name):
    def greating(tenplate):
        return tenplate.replace("%name%", name)
    return greating

def make_word_formater(template):
    def word_formater(world, _index):
        return template.replace("%world%",world).replace("%index%", str(_index + 1))
    return word_formater

def proccess_sentence(sentence, word_formater):
    words = sentence.split(" ")
    for _index, word in enumerate(words):
        print(word_formater(word, _index))





if __name__ == "__main__":
    print("cli handling")


    print(adding(5)) #adding függvény

    print(type([1, 2]))
    print(remove_null([0, 1, 2, 3, 4, 5])) #remove null

    d = {'a': 0, 'b': 1} # valami
    print(d)
    print(d['b'])

print(is_prime("asd"))  # prím szám e
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))

'''pg = prime_gen()
for _ in range(10):
    prime = next(pg) # prím szám genetártor
    print(prime)'''


hello = make_greating("World")
print(hello("Hello %name%"))

