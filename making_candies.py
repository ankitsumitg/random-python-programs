def minimum_passes(m, w, p, n):
    can = 0
    pas = 0
    while True:
        pas += p // (m * w)
        new_pas = p // (m * w)
        can += m * w * new_pas
        if can < p:
            pas += 1
            can += m * w
        if can >= n:
            break
        if can + m * w >= n:
            pas += 1
            break
        to_buy = can // p
        can -= to_buy * p
        if m + to_buy < w:
            m += to_buy
        elif w + to_buy < m:
            w += to_buy
        else:
            if w > m:
                need = w - m
                m += need
                to_buy -= need
            else:
                need = m - w
                w += need
                to_buy -= need
            if to_buy % 2 == 0:
                w += to_buy // 2
                m += to_buy // 2
            else:
                w += to_buy // 2 + 1
                m += to_buy // 2
    return pas


def check_more_or_less_rounds(machines, workers, price, target, mid):
    if machines * workers >= target:
        # We have more work power than needed, so keep looking left wise
        return True

    mid -= 1

    if mid == 0:
        # Have we found the pivot?
        return False

    curr = machines * workers

    while True:
        # Given the current workload, compute the remaining rounds
        remaining = target - curr
        remaining_rounds = (remaining - 1) // (machines * workers) + 1

        # We have more rounds than needed, so keep looking left wise
        if remaining_rounds <= mid:
            return True

        # if this production round yield less than the 'price'
        if curr < price:
            # compute how many rounds to produce enough to match 'price'
            remaining = price - curr
            remaining_rounds = (remaining - 1) // (machines * workers) + 1

            mid -= remaining_rounds

            # We don't have enough rounds to par the price, so keep looking to the right
            if mid < 1:
                return False

            curr += remaining_rounds * machines * workers

        # Do the hire or purchase
        if machines > workers:
            workers += 1
        else:
            machines += 1

        # Do debit the price
        curr -= price


# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    min_rounds = 1
    max_rounds = n

    while min_rounds < max_rounds:
        mid = (min_rounds + max_rounds) // 2

        if check_more_or_less_rounds(m, w, p, n, mid):
            max_rounds = mid
        else:
            min_rounds = mid + 1

    return min_rounds


print(minimumPasses(1, 3, 92, 373))
