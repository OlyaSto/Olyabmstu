import random


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)


def main():
    gen = gen_random(9, 1, 10)
    for i in gen:
        print(i, end =' ')


if __name__ == "__main__":
    main()