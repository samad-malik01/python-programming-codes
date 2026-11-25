import sys

def main():
    data = sys.stdin.read().split()
    m, n = int(data[0]), int(data[1])
    coupons = data[2:2 + m]
    scans = data[2 + m:2 + m + n]

    has_coupon = set(coupons)
    used = set()
    accepted = repeat = invalid = 0

    for sid in scans:
        if sid not in has_coupon:
            invalid += 1
        elif sid in used:
            repeat += 1
        else:
            used.add(sid)
            accepted += 1

    unused = sorted(has_coupon - used)

    print(accepted, repeat, invalid)
    print(" ".join(unused) if unused else "NONE")

main()
