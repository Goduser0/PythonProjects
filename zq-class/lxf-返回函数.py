# Noel Stallworth
# TIME: 2021/9/30 23:00
def lazy_sum(*agrs):
    def sum():
        ax = 0
        for cell in agrs:
            ax += cell
        return ax
    return sum


a = lazy_sum(1, 2, 3, 4)
print(a)

b = lazy_sum(1, 2, 3, 4)
print(a == b)  # False

print(a())
