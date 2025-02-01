def common_divisors(a, b):
        divisors_a = set()
        for i in range(1, a + 1):
            if a % i == 0:
                divisors_a.add(i)
        divisors_b = set()
        for i in range(1, b + 1):
            if b % i == 0:
                divisors_b.add(i)
                
        common = divisors_a & divisors_b
        return ";".join(map(str, sorted(common)))

a, b = 4, 8

print(common_divisors(a, b))