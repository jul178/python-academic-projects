import urllib.request
def read_input_file(url: str, number: int) -> list[list[str]]:
    """
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], \
['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    content = []
    with open(url, 'r', encoding='utf-8') as file:
        for i in range(1, number + 1):
        #     line = file.readline()
        # content.append(line)
            for line in file:
                if line.startswith(str(i)):
                    line = line.strip().split()
                    num = line[0]
                    name = ' '.join(line[1:4])
                    sum_point = line[6]
                    file.readline()
                    file.readline()
                    avg = file.readline()[-6:-1]
                    content.append([num, name, '+', sum_point, avg])
    return content


def write_csv_file(url: str):
    '''write info to csv file with the path total.csv'''
    pass


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
