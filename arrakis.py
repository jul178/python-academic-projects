"""Arracis"""
def transform_ticket(ticket: str) -> tuple[int] | None:
    """ Parse a railway ticket code and convert it into a tuple containing
    (car_number, compartment_number, seat_number).
    Args:
        ticket (str): Ticket code string of the form 7×{'Г'|'Х'} followed by
                  3×{'Л'|'П'}. Example: "ГГХГХХГЛЛП".

    Returns:
        tuple[int, int, int] | None:
            A 3-tuple `(wagon, coupe, seat)` (all 1-based indices) for a valid
            ticket, or `None` if `ticket` is invalid.

    >>> transform_ticket("ГГХГХХГЛЛП")
    (3, 7, 2)
    >>> transform_ticket("ГГХГХХЛЛГП")
    >>> transform_ticket("Вагон 7, місце 3")
    >>> transform_ticket("ХХХХХХХЛЛП")
    (16, 8, 2)
    >>> transform_ticket("ГГГГГГГЛЛП")
    (1, 1, 2)
    """
    if not isinstance(ticket, str) or len(ticket) != 10:
        return None
    if not all(ch in ("Г", "Х") for ch in ticket[:7]):
        return None
    if not all(ch in ("Л", "П") for ch in ticket[7:]):
        return None
    carriages = 16
    compartments = 128
    s_comp = 1
    f_comp = 128
    s_seat = 1
    f_seat = 8
    for ch in ticket[:7]:
        if ch == 'Г':
            mid = (s_comp + f_comp) // 2
            f_comp = mid
        elif ch == 'Х':
            mid = (s_comp + f_comp) // 2
            s_comp = mid+1
        else:
            return None
    for ch in ticket[7:]:
        if ch == 'Л':
            mid = (s_seat + f_seat) // 2
            f_seat = mid
        elif ch == 'П':
            mid = (s_seat + f_seat) // 2
            s_seat = mid + 1
        else:
            return None

    carriage = int((f_comp - 1)/ (compartments // carriages) + 1)
    compartment = (f_comp - 1) % (compartments // carriages) + 1
    return (carriage, compartment, f_seat)


# print(transform_ticket("ГГХГХХГЛЛП"))



# if ch == 'Г':
            #     if isinstance(compartment, list):
            #         new_compartment = short_compartment[:(len(compartment) // 2) + 1]
            #         short_compartment = new_compartment
            #     else:
            #         new_compartment = compartment // 2
            #         short_compartment = list(range(1, new_compartment))
            #     compartment = short_compartment
            # elif ch == 'Х':
            #     if isinstance(compartments, list):
            #         new_compartment = short_compartment[:(len(compartment) // 2) + 1]
            #         short_compartment = new_compartment
            #     else:
            #         start_compartment = compartment // 2
            #         short_compartment = list(range(start_compartment, compartment))
            #     compartments = short_compartment
            # else:
            #     return None

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
