from practice_6.cls_validate_types import User
from typing import get_type_hints

def main():
    User(email='a', age=18)


if __name__ == '__main__':
    main()
