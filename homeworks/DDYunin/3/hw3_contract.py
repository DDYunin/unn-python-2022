class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def mydecorator(mfunction):
        def wrapped(*args):
            # вызов функции
            if return_type is not None:
                if return_type != type(mfunction(*args)):
                    raise ContractError("Error! Uncorrect return type")
            if arg_types != None:
                for arg, arg_type in zip(args, arg_types):
                    if type(arg) != arg_type and arg_type != Any:
                        raise ContractError("Error! Uncorrect arg_types")
            try:
                mfunction(*args)
            except:
                raise raises
            return mfunction(*args)
        return wrapped
    return mydecorator

if __name__ == '__main__':
    @contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
    def div(first, second):
        return first / second

    print(div(1, 2))  # ok
    # print(div(1, 0))  # raises ZeroDisionError
    # print(div(1, None))  # raises ContractError from TypeError


    @contract(arg_types=(int, int), return_type=int)
    def add_two_numbers(first, second):
        return first + second

    print(add_two_numbers(1, 2))  # ok

    @contract(arg_types=(str, str))
    def add_str(first, second):
        return first + second

    print(add_str("Hello", "World"))

    @contract(arg_types=(int, Any))
    def add_two_numbers2(first, second):
        return first + second

    print(add_two_numbers2(1, 2))  # ok
    print(add_two_numbers2(1, 3.4))  # ok
    # print(add_two_numbers2(2.1, 1))  # raises ContractError