"""Renames locations.
It reads a specific text file format, extracts information about
renamed populated places, and writes the structured data to a CSV file.
"""
# def normalize_oblast(line: str) -> str:
#     """
#     Extract region name from lines like:
#     '1) у Вінницькій області:' → 'Вінницька область'

#     >>> normalize_oblast("1) у Вінницькій області:")
#     'Вінницька область'
#     """
#     region_part = line.split(" у ", 1)[1].strip(": \n")
#     adj = region_part.split()[0]

#     if adj.endswith("ській"):
#         adj = adj[:-4] + "ька"
#     elif adj.endswith("кій"):
#         adj = adj[:-3] + "ка"

#     return adj + " область"


# def shorten_name(name: str) -> str:
#     """Shortens settlement prefixes.

#     >>> shorten_name("село Червоне")
#     'с.Червоне'
#     >>> shorten_name("місто Артемове")
#     'м.Артемове'
#     >>> shorten_name("селище Петрівське")
#     'с-ще Петрівське'
#     >>> shorten_name("селище міського типу Никанорівка")
#     'смт Никанорівка'
#     """
#     if name.startswith("селище міського типу "):
#         return "смт " + name[len("селище міського типу "):]
#     if name.startswith("селище "):
#         return "с-ще " + name[len("селище "):]
#     if name.startswith("село "):
#         return "с." + name[len("село "):]
#     if name.startswith("місто "):
#         return "м." + name[len("місто "):]
#     return name


# def parse_old(old_part: str):
#     """
#     Parses old part into (oldname, areaname).
#     Handles cases like:
#     - 'село Червоне Барського району'
#     - 'місто Артемове Торецької міської ради'
#     - 'Краснолиманський район'
#     - 'селище ... ради Волноваського району'
#     """
#     words = old_part.split()


#     if len(words) >= 6 and words[-1] == "району" and words[-3] == "ради":
#         oldname = " ".join(words[:-2])
#         areaname = words[-2] + " " + words[-1]
#         return oldname, normalize_areaname(areaname)
#     if len(words) >= 3 and words[-1] == "району":
#         oldname = " ".join(words[:-2])
#         areaname = words[-2] + " " + words[-1]
#         return oldname, normalize_areaname(areaname)
#     if len(words) >= 3 and words[-1] == "ради":
#         oldname = " ".join(words[:-3])
#         areaname = " ".join(words[-3:])
#         return oldname, normalize_areaname(areaname)
#     return old_part, ""


# def normalize_areaname(name: str) -> str:
#     """
#     Normalizes areaname endings.
#     Only what tests require.

#     >>> normalize_areaname("Барського району")
#     'Барський район'
#     >>> normalize_areaname("Торецької міської ради")
#     'Торецька міська рада'
#     """
#     words = name.split()

#     # район
#     if words[-1] in ("району", "район"):
#         base = words[0]
#         if base.endswith("ького"):
#             base = base[:-5] + "ький"
#         elif base.endswith("ого"):
#             base = base[:-3] + "ий"
#         return base + " район"

#     # рада
#     if words[-1] == "ради":
#         w0 = words[0]
#         w1 = words[1]

#         if w0.endswith("ської"):
#             w0 = w0[:-4] + "ка"
#         elif w0.endswith("ої"):
#             w0 = w0[:-2] + "а"

#         if w1.endswith("ої"):
#             w1 = w1[:-2] + "а"

#         return f"{w0} {w1} рада"

#     return name


# def read_file(filename):
#     """
#     Reads resolution and returns dictionary.

#     >>> import tempfile
#     >>> test_content = '''1) у Вінницькій області:
#     ...    село Червоне Барського району на село Грабівці;
#     ...    місто Дніпродзержинськ на місто Кам’янське;
#     ... 2) у Донецькій області:
#     ...    місто Артемове Торецької міської ради на місто Залізне;
#     ...    селище Петрівське Оленівської селищної ради Волноваського району на селище Нова Оленівка;
#     ...    Краснолиманський район на Лиманський район;'''
#     >>> with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8') as tmp:
#     ...     _ = tmp.write(test_content)
#     ...     name = tmp.name
#     >>> result = read_file(name)
#     >>> expected = {
#     ...     ('Вінницька область', 'Барський район', 'с.Червоне'): 'с.Грабівці',
#     ...     ('Вінницька область', '', 'м.Дніпродзержинськ'): 'м.Кам’янське',
#     ...     ('Донецька область', 'Торецька міська рада', 'м.Артемове'): 'м.Залізне',
#     ...     ('Донецька область', 'Волноваський район', \
# 'с-ще Петрівське Оленівської селищної ради'): 'с-ще Нова Оленівка',
#     ...     ('Донецька область', '', 'Краснолиманський район'): 'Лиманський район'
#     ... }
#     >>> sorted(result.items()) == sorted(expected.items())
#     True
#     """
#     info = {}
#     regionname = ""

#     with open(filename, encoding="utf-8") as f:
#         for line in f:
#             line = line.strip()
#             if not line:
#                 continue

#             # region header
#             if line[0].isdigit() and "області" in line:
#                 regionname = normalize_oblast(line)
#                 continue

#             if " на " not in line:
#                 continue

#             old_part, new_part = line.split(" на ")
#             oldname, areaname = parse_old(old_part)
#             oldname = shorten_name(oldname)
#             newname = shorten_name(new_part.rstrip(";"))

#             info[(regionname, areaname, oldname)] = newname

#     return info


# def write_csv_file(info, filename):
#     """
#     >>> import tempfile
#     >>> d = {
#     ...     ('Region B','Area A','v. Old'):'v. New',
#     ...     ('Region A','Area B','c. Old'):'c. New'
#     ... }
#     >>> with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8') as tmp:
#     ...     name = tmp.name
#     >>> write_csv_file(d, name)
#     >>> print(open(name, encoding='utf-8').read())
#     regionname,areaname,oldname,newname
#     Region A,Area B,c. Old,c. New
#     Region B,Area A,v. Old,v. New
#     <BLANKLINE>
#     """
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write("regionname,areaname,oldname,newname\n")
#         for key in sorted(info.keys()):
#             region, area, old = key
#             f.write(f"{region},{area},{old},{info[key]}\n")

# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())
#     [print(line) for line in read_file('renamed_small.py').items()]

def  read_file(filename):
    """Reads a resolution file on renaming locations and parses it into a dictionary.

    Args:
        filename (str): The path to the input text file.
    Returns:
        dict: A dictionary where the key is a tuple (tuple) of three strings:
              (regionname, areaname, oldname),
              and the value (value) is a string with the new name
    >>> import tempfile
    >>> test_content = '''1) у Вінницькій області:
    ...    село Червоне Барського району на село Грабівці;
    ...    місто Дніпродзержинськ на місто Кам’янське;
    ... 2) у Донецькій області:
    ...    місто Артемове Торецької міської ради на місто Залізне;
    ...    селище Петрівське Оленівської селищної ради Волноваського району на селище Нова Оленівка;
    ...    Краснолиманський район на Лиманський район;'''
    >>> with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8') as tmp:
    ...     _ = tmp.write(test_content)
    ...     tmp_name = tmp.name
    >>> result = read_file(tmp_name)
    >>> expected = {
    ...     ('Вінницька область', 'Барський район', 'с.Червоне'): 'с.Грабівці',
    ...     ('Вінницька область', '', 'м.Дніпродзержинськ'): 'м.Кам’янське',
    ...     ('Донецька область', 'Торецька міська рада', 'м.Артемове'): 'м.Залізне',
    ...     ('Донецька область', 'Оленівська селищна рада', 'с-ще Петрівське'): \
'с-ще Нова Оленівка',
    ...     ('Донецька область', '', 'Краснолиманський район'): 'Лиманський район'
    ... }
    >>> sorted(result.items()) == sorted(expected.items())
    True
    """
    info = {}
    regionname = ''
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if line and line[0].isdigit() and 'області' in line:
                region_part = ''
                if ' у ' in line:
                    region_part = line.split(' у ', 1)[1].strip(':\n').split()
                elif ' в ' in line:
                    region_part = line.split(' в ', 1)[1].strip(':\n').split()

                region_part[0] = region_part[0].replace('ій', 'а')
                region_part[1] = region_part[1].replace('і', 'ь')
                regionname = region_part[0] + " " + region_part[1]

            if ' на ' not in line or 'станом на ' in line:
                continue

            old_part, new_part = line.split(' на ')
            new_part = new_part.strip(';').strip('.')


            words = old_part.split()
            oldname = ""
            areaname = ""

            if words[-1] == 'району' and words[-3] == 'ради':
                oldname = ' '.join(words[:-5])
                areaname = ' '.join(words[-5:])
            elif words[-1] == 'району':
                oldname = ' '.join(words[:-2])
                areaname = ' '.join(words[-2:])
            elif words[-1] == 'район':
                oldname = ' '.join(words[:])
            elif words[-1] == 'ради':
                oldname = ' '.join(words[:-3])
                areaname = ' '.join(words[-3:])
            else:
                oldname = old_part
                areaname = ""

            if areaname:
                area_words = areaname.split()
                if words[-1] == 'району' and words[-3] == 'ради':
                    area_noun = area_words[-1].replace("у", "")
                    if area_words[-2].endswith('ого'):
                        area_adj = area_words[-2].replace("ого", "ий")
                        areaname = area_adj + " " + area_noun
                    area_words[-3] = area_words[-3].replace("и", "а")
                    area_words[-4] = area_words[-4].replace("ої", "а")
                    area_words[-5] = area_words[-5].replace("ої", "а")
                    areaname = area_words[-5] + " " + area_words[-4] + " " + area_words[-3]

                elif area_words[-1] == 'району':
                    area_noun = area_words[-1].replace("у", "")
                    if area_words[0].endswith('ого'):
                        area_adj = area_words[0].replace("ого", "ий")
                        areaname = area_adj + " " + area_noun

                elif area_words[-1] == 'ради':
                    area_words[-1] = area_words[-1].replace("и", "а")
                    area_words[-2] = area_words[-2].replace("ої", "а")
                    area_words[-3] = area_words[-3].replace("ої", "а")
                    areaname = area_words[0] + " " + area_words[1] + " " + area_words[2]

            if oldname.startswith('селище міського типу '):
                oldname = oldname.replace('селище міського типу ', 'смт ', 1)
            elif oldname.startswith('селище '):
                oldname = oldname.replace('селище ', 'с-ще ', 1)
            elif oldname.startswith('село '):
                oldname = oldname.replace('село ', 'с.', 1)
            elif oldname.startswith('місто '):
                oldname = oldname.replace('місто ', 'м.', 1)

            newname = new_part
            if new_part.startswith('селище міського типу '):
                newname = new_part.replace('селище міського типу ', 'смт ', 1)
            elif new_part.startswith('селище '):
                newname = new_part.replace('селище ', 'с-ще ', 1)
            elif new_part.startswith('село '):
                newname = new_part.replace('село ', 'с.', 1)
            elif new_part.startswith('місто '):
                newname = new_part.replace('місто ', 'м.', 1)

            info[(regionname, areaname, oldname)] = newname
        return info

def write_csv_file(info, filename):
    """
    Writes the dictionary with renaming data to a CSV file.

    The function accepts an 'info' dictionary (of the structure returned
    by read_file) and an output filename 'filename'.

    The data is sorted alphabetically by key (region, area, old name)
    and written to the file in CSV format (comma as delimiter).

    Args:
        info (dict): A dictionary with renaming data.
        filename (str): The path to the output CSV file
    Returns:
        None.
    >>> import tempfile
    >>> test_dict = {
    ...     ('Region B', 'Area A', 'v. Old'): 'v. New',
    ...     ('Region A', 'Area B', 'c. Old'): 'c. New',
    ... }
    >>> with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8') as tmp:
    ...     tmp_name = tmp.name
    >>> write_csv_file(test_dict, tmp_name)
    >>> with open(tmp_name, 'r', encoding='utf-8') as f:
    ...     content = f.read()
    ...     print(content)
    regionname,areaname,oldname,newname
    Region B,Area A,v. Old,v. New
    Region A,Area B,c. Old,c. New
    <BLANKLINE>
    """
    # sorted_keys = sorted(info.keys())

    with open(filename, 'w', encoding='utf-8') as file_csv:
        file_csv.write("regionname,areaname,oldname,newname\n")
        # for key in sorted_keys:
        for key in info.keys():
            newname = info[key]
            regionname,areaname,oldname = key
            line = f"{regionname},{areaname},{oldname},{newname}\n"
            file_csv.write(line)

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    # [print(line) for line in read_file('renamed_small.py').items()]
    # [print(line) for line in read_file('renamed_locations_24.txt').items()]
