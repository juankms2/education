def sum_number(num):
    try:
        return int(num) + 5
    except ValueError as err:
        # return err
        raise err
