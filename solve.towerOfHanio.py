# def tower_of_hanoi(n, source, target, auxiliary):
#     if n == 1:
#         return print("Move disk 1 from rod", source, "to rod", target)
    
#     tower_of_hanoi(n-1, source, auxiliary, target)
#     print("Move disk", n, "from rod", source, "to rod", target)
#     tower_of_hanoi(n-1, auxiliary, target, source)

# n = 3  #Number of disks
# tower_of_hanoi(n, 'A', 'C', 'B')


def hanoi(n, src, via, dst):
    if n == 1:
        print(f"{src} -> {dst}")
    else:
        hanoi(n - 1, src, dst, via)
        hanoi(1, src, via, dst)
        hanoi(n - 1, via, src, dst)

N = int(input())
hanoi(N, "A", "B", "C")