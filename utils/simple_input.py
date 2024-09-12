def get_boolean_input(input_str: str, default_option: bool|None = None) -> bool:
    while True:
        return_str = input(input_str)

        if not return_str:
            if default_option is not None:
                return default_option
            continue

        if return_str.lower().strip() in ['n', 'no']:
            return False

        if return_str.lower().strip() in ['y', 'yes']:
            return True


def get_integer_input(input_str: str, default_option: int | None = None) -> int:
    while True:
        return_str = input(input_str)

        if not return_str:
            if default_option is not None:
                return default_option
            continue

        if not return_str.strip().isnumeric():
            continue

        return int(return_str.strip())


def get_string_input(input_str: str, default_option: str | None = None) -> str:
    while True:
        return_str = input(input_str)

        if not return_str:
            if default_option is not None:
                return default_option
            continue

        return return_str
