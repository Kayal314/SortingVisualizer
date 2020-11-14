import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((1550, 800))
array = [71, 46, 34, 30, 11, 98, 95, 45, 93, 56, 32, 92, 32, 58, 62, 73, 68, 91, 23, 87, 77, 76, 87, 73, 3, 1, 6, 68,
         96, 42, 1, 29, 40, 56, 85, 22, 92, 58, 60, 44, 99, 82, 12, 13, 10, 85, 45, 78, 62, 86]
pygame.display.set_caption("Algo Visualizer")
color = (21, 171, 191)
font = pygame.sysfont.SysFont("Arial", 20, False, False)


def bubble_sort(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                draw_array(arr)


def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_val = arr[i]
        position = i
        for j in range(i + 1, n):
            if array[j] < min_val:
                min_val = array[j]
                position = j
            draw_array(arr)
        swap(arr, position, i)
    draw_array(arr)


def merge_sort(arr, s, e):
    if s < e:
        m = int((s + e) / 2)
        merge_sort(arr, s, m)
        merge_sort(arr, m + 1, e)
        merge(arr, s, m, e)


def merge(arr, s, m, e):
    a = []
    b = []
    for i in range(s, m + 1):
        a.append(arr[i])
    for i in range(m + 1, e + 1):
        b.append(arr[i])
    i = 0  # counter for a
    j = 0  # counter for b
    na = len(a)
    nb = len(b)
    for k in range(s, e + 1):
        if i == na:
            arr[k] = b[j]
            j += 1
        elif j == nb:
            arr[k] = a[i]
            i += 1
        else:
            if a[i] < b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
        draw_array(arr)


def quick_sort(arr, s, e):
    if s < e:
        pivot = get_pivot(arr, s, e)
        quick_sort(arr, s, pivot - 1)
        quick_sort(arr, pivot + 1, e)


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def get_pivot(arr, s, e):
    pivot = random.randrange(s, e + 1)
    swap(arr, s, pivot)
    pivot_val = arr[s]
    j = s + 1
    for i in range(s + 1, e + 1):
        draw_array(arr)
        if arr[i] < pivot_val:
            swap(arr, i, j)
            j += 1
    swap(arr, j - 1, s)
    draw_array(arr)
    return j - 1


def unsort(arr):
    for i in range(0, 50):
        arr[i] = random.randrange(1, 100)
    draw_array(arr)


def draw_array(new_arr):
    screen.fill((121, 208, 208))
    for i in range(0, 50):
        initial_array((i + 1) * 30, new_arr[i] * 7)
    pygame.display.update()


def draw_reset_button():
    rect = pygame.draw.rect(screen, (121, 208, 208), (1350, 10, 100, 35), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("Unsort", True, (12, 104, 109), None)
    screen.blit(text, rect)


def draw_ms_button():
    rect = pygame.draw.rect(screen, (121, 208, 208), (100, 10, 100, 35), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("MergeSort", True, (12, 104, 109), None)
    screen.blit(text, rect)


def draw_qs_button():
    rect = pygame.draw.rect(screen, (121, 208, 208), (300, 10, 100, 35), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("QuickSort", True, (12, 104, 109), None)
    screen.blit(text, rect)


def draw_bs_button():
    rect = pygame.draw.rect(screen, (121, 208, 208), (500, 10, 110, 35), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("BubbleSort", True, (12, 104, 109), None)
    screen.blit(text, rect)


def draw_ss_button():
    rect = pygame.draw.rect(screen, (121, 208, 208), (710, 10, 150, 35), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("SelectionSort", True, (12, 104, 109), None)
    screen.blit(text, rect)


def initial_array(x0, height):
    rect = (x0, 60, 15, height)
    pygame.draw.rect(screen, color, rect, 0)


if __name__ == '__main__':
    draw_array(array)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 100 < pos[0] < 200 and 10 < pos[1] < 45:
                    merge_sort(array, 0, len(array) - 1)
                elif 300 < pos[0] < 400 and 10 < pos[1] < 45:
                    quick_sort(array, 0, len(array) - 1)
                elif 500 < pos[0] < 610 and 10 < pos[1] < 45:
                    bubble_sort(array)
                elif 1350 < pos[0] < 1450 and 10 < pos[1] < 45:
                    unsort(array)
                elif 710 < pos[0] < 860 and 10 < pos[1] < 45:
                    selection_sort(array)
        draw_reset_button()
        draw_ms_button()
        draw_qs_button()
        draw_bs_button()
        draw_ss_button()
        pygame.display.update()
