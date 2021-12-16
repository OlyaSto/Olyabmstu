def print_result(func_to_decorate):

    def decorated_func(*args):
        print(func_to_decorate.__name__)

        result = func_to_decorate(*args)

        if type(result) is list:
            for i in result:
                print(i)
        elif type(result) is dict:
            for i in result:
                print(i, result.get(i), sep=' = ')
        else:
            print(result)

        return result

    return decorated_func


@print_result
def f1():
    return 1


@print_result
def f2():
    return 'olya'


@print_result
def f3():
    return {'a': 1, 'b': 2}


@print_result
def f4():
    return [1, 2]


def main():
    f1()
    f2()
    f3()
    f4()


if __name__ == '__main__':
    main()