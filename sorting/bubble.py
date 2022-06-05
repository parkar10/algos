
def bubble_sort(a: list) -> list:
    """
    Bubble sort

    Args:
        a (list): input list

    Returns:
        list: sorted list
    """
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp




def inverse_bubble_sort(a: list) -> list:
    """
    Bubble sort

    Args:
        a (list): input list

    Returns:
        list: inversely sorted list
    """
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] < a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp


a = [1, 3, 8, 2, 9, 2, 5, 6]
bubble_sort(a)
print(a)
inverse_bubble_sort(a)
print(a)
