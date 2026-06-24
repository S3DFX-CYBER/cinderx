from __static__ import int64

FAILURES = 0


def phi_loop(flag: bool, start: int64, alt: int64):
    x: int64

    if flag:
        x = start
    else:
        x = alt

    i: int64 = 0

    while i < 10000:
        x += 1
        i += 1

    return x


def nested_phi(flag1: bool, flag2: bool, a: int64, b: int64):
    if flag1:
        x = a
    else:
        x = b

    if flag2:
        y = x
    else:
        y = x + 1

    return y


def verify():
    global FAILURES

    for i in range(1000):

        r1 = phi_loop(True, i, 999)
        expected1 = i + 10000

        if r1 != expected1:
            print("FAIL phi_loop(TRUE)", i, r1, expected1)
            FAILURES += 1
            return

        r2 = phi_loop(False, 999, i)
        expected2 = i + 10000

        if r2 != expected2:
            print("FAIL phi_loop(FALSE)", i, r2, expected2)
            FAILURES += 1
            return

        r3 = nested_phi(True, False, i, 123)
        expected3 = i + 1

        if r3 != expected3:
            print("FAIL nested_phi", i, r3, expected3)
            FAILURES += 1
            return

    print("PASS")


if __name__ == "__main__":
    verify()
