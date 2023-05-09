#task____1
print('You have 100 cats.')
def get_cats_with_hats(n: int) -> list[int]:
    cats = [False] * n
    for i in range(1, n+1):
        for j in range(i-1, n, i):
            cats[j] = not cats[j]
    return [i+1 for i in range(n) if cats[i]]

print(get_cats_with_hats(100))