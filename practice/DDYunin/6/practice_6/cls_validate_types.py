import typing

class ValidateTypes(type):
    def __new__(cls, name, bases, kwargs):
        kwargs['__init__'] = cls._init
        klass = super().__new__(cls, name, bases, kwargs)
        klass.__validators__ = typing.get_type_hints(klass)
        return klass

    def _init(self, **kwargs):
        for name, typ in self.__class__.__validators__.items():
            passed = kwargs[name]
            if not isinstance(passed, typ):
                raise TypeError(
                    'Passed {name} is not instance of {typ}'.format(
                        name=name,
                        typ=typ,
                    ),
                )

class User(object, metaclass=ValidateTypes):
    x: int
    y: str

print(User(x=1, y='a'))
print(User(x='a', y='b'))
