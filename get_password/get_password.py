"""
Get password from a chain of files.
"""

def read_file(filename: str) -> tuple[str, int, str]:
    """
    Read a chained file and extract three logical blocks:
    a multi-line, space-padded password fragment, ordinal number and the next filename.

    The function tolerates arbitrary noise before the first '#' and after the
    last '#'.

    Parameters
    ----------
    filename : str
        Path to the file.

    Returns
    -------
    tuple[str, int, str]
        (raw_password_block, ordinal number, next_filename)

    Examples
    --------
    >>> simple_text = '#\\nA B\\n C\\n#\\n2\\n#\\nnext.txt\\n#'
    >>> print(simple_text)
    #
    A B
     C
    #
    2
    #
    next.txt
    #
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='r+', delete=False) as f:
    ...     _ = f.write(simple_text)
    >>> read_file(f.name)
    ('A B\\n C', 2, 'next.txt')

    >>> read_file('start.txt')
    ('A  A  N  C  Z\\n A  C  z  1\\n  A  3  a  l', 0, 'file1.txt')
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        string = ''.join(lines)
        # print(repr(string))

        string = string.split('#', 1)[1].strip() # del everything before first #
        # print(repr(string))
        i = string.rfind("#")
        # print(i)
        string = string[:i].strip() # dont take everything that after last #
        # print(repr(string))
        list_cleaned = string.split("\n#\n")
        # print(list_cleaned)
        raw_password_block = list_cleaned[0]
        ordinal_number = int(list_cleaned[1])
        next_filename = list_cleaned[2]

    return (raw_password_block, ordinal_number, next_filename)


def decode_raw_password(text: str) -> str:
    """
    Decodes a visually formatted "rail fence" block of text into a continuous string.
    The function reads characters column by column (top to bottom), ignoring spaces
    and blank lines. The height (number of rows) can be different.

    Parameters
    ----------
    text : str
        Multiline string where each line represents one "rail" or level
        of the encoded text. Spaces are used only for visual alignment.

    Returns
    -------
    str
        The decoded continuous string.

    Example:
    --------
    >>> decode_raw_password('A  A  N  C  Z\\n A  C  z  1\\n  A  3  a  l')
    'AAAAC3NzaC1lZ'
    >>> decode_raw_password('D  N  5  A  u\\n I  T  A  A\\n  1  E  A  I')
    'DI1NTE5AAAAIu'
    >>> decode_raw_password('p  n  6  x  w\\n T  V  e  4\\n  3  b  Z  Y')
    'pT3nVb6eZx4Yw'
    """
    list_row = text.split("\n")
    # print(list_row)
    decoded_string = ''
    raw_rows = []
    for row in list_row:
        row = row.replace(" ", "")
        # print(row)
        raw_rows.append(row)
    # print(raw_rows)

    max_lenght = max(len(row) for row in raw_rows)

    for col in range(max_lenght):
        for row in raw_rows:
            if col < len(row):
                ch = row[col]
                decoded_string += ch

    return decoded_string


def collect_raw_passwords(startname: str) -> list[tuple[int, str, str]]:
    '''
    Traverse the entire chain of files starting from `startname`, decode each
    password fragment, and return a list of tuples containing the filename and its
    decoded fragment.

    Each tuple in the result represents one step in the chain:
        (ordinal number, current_filename, decoded_fragment)

    The traversal continues until a file specifies "END" as the next filename.

    Parameters
    ----------
    startname : str
        The name or path of the first file in the chain.

    Returns
    -------
    list[tuple[str, int, str]]
        A list of pairs, where:
          - the first element is the ordinal number of the fragment,
          - the second element is the filename processed,
          - the third element is the decoded part of the password.

    Examples
    --------
    >>> collect_raw_passwords('start.txt')
    [(0, 'start.txt', 'AAAAC3NzaC1lZ'), (1, 'file1.txt', 'DI1NTE5AAAAIu'), \
(3, 'file3.txt', 'Qx9vL2m5sK8rY'), (2, 'file2.txt', 'pT3nVb6eZx4Yw'), \
(4, 'end.txt', '7Hc2JqR5tUvWx')]
    '''
    info = []
    while startname != 'END':
        raw_password_block, ordinal_number, next_filename = read_file(startname)
        decoded_password = decode_raw_password(raw_password_block)
        info.append((ordinal_number, startname, decoded_password))
        startname = next_filename
    return info

def write_password_file(raw_passwords: list[tuple[int, str, str]],
                       output_file: str) -> None:
    """
    Write all collected password fragments to a text file, followed by the
    final combined password according to the ordinal numbers.

    The file will contain:
      1. A header "Gathered fragments:".
      2. One line per fragment in the format "<ordinal number>,<filename>,<fragment>".
      3. A blank line with the label "Final password:".
      4. The complete password

    Parameters
    ----------
    raw_passwords : list[tuple[int, str, str]]
        List of tuples (ordinal number, filename, fragment), as returned by `collect_raw_passwords`.
    output_file : str
        Path to the destination file where the output will be written.

    Returns
    -------
    None

    Examples
    --------
    >>> raw_passwords = [(0, 'start.txt', 'AAAAC3NzaC1lZ'), (1, 'file1.txt', 'DI1NTE5AAAAIu'), \
(3, 'file3.txt', 'Qx9vL2m5sK8rY'), (2, 'file2.txt', 'pT3nVb6eZx4Yw'), \
(4, 'end.txt', '7Hc2JqR5tUvWx')]
    >>> write_password_file(raw_passwords, 'password.txt')
    >>> with open('password.txt', 'r', encoding='utf-8') as f:
    ...     print(f.read())
    Gathered fragments:
    0,start.txt,AAAAC3NzaC1lZ
    1,file1.txt,DI1NTE5AAAAIu
    3,file3.txt,Qx9vL2m5sK8rY
    2,file2.txt,pT3nVb6eZx4Yw
    4,end.txt,7Hc2JqR5tUvWx
    Final password:
    AAAAC3NzaC1lZDI1NTE5AAAAIupT3nVb6eZx4YwQx9vL2m5sK8rY7Hc2JqR5tUvWx
    """
    gathered_str = ''
    final_password = ''
    for el in raw_passwords:
        gathered_str += f'{el[0]},{el[1]},{el[2]}\n'

    sorted_str = sorted(raw_passwords)
    # print(sorted_str)
    for elem in sorted_str:
        final_password += elem[2]

    result = "Gathered fragments:\n" + gathered_str + "Final password:\n" + final_password
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    # print(write_password_file([(0, 'start.txt', 'AAAAC3NzaC1lZ'),
    # (1, 'file1.txt', 'DI1NTE5AAAAIu'), (3, 'file3.txt', 'Qx9vL2m5sK8rY'),
    # (2, 'file2.txt', 'pT3nVb6eZx4Yw'), (4, 'end.txt', '7Hc2JqR5tUvWx')], 'output.txt'))
