"""For and range()"""

xs: list[str] = ["w", "x", "y", "z"]

idx: int = 0
while idx < len(xs):
    print(xs[idx])
    idx += 1

for i in xs:
    print(i)

pets: list[str] = ["Louie", "Bo", "Bear"]

for i in pets:
    print(f"Good boy, {i}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for name in range(len(names)):
    print(f"{name}:{names[name]}")
