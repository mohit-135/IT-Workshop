# # n = int(input("Enter n: "))

# # for i in range(6):
# #     for j in range(5-i):
# #         print(" ", end="")
# #     if(i == 0):
# #         for j in range(12):
# #             print("*  " , end="")
# #         print()
# #     else:
# #         print("*", end="")
# #         for j in range(2 * i - 1):
# #             print(" ", end="")
# #         print("*")

# #     if(i == 5):
# #             for j in range(13):
# #                 print("*  " , end="")
# #             print()

# # print("    * * * * * * * * * * * * * * * *")
# # print("   * *                            *")
# # print("  *   *                           *")
# # print(" *     *                          *")
# # print("* * * * * * * * * * * * * * * * * *")
# # print("*       *                         *")
# # print("*       *                         *")
# # print("*       *                         *")
# # print("*       *          * * *          *")
# # print("*       *          *   *          *")
# # print("*       *          *   *          *")
# # print("*       *          *   *          *")
# # print("* * * * * * * * * * * * * * * * * *")


# n = 5

# # Roof
# for i in range(n):
#     for j in range(n - i - 1):
#         print("  ", end="")

#     for j in range(2 * i + 1):
#         print("* ", end="")

#     print()

# # Upper wall
# for i in range(4):
#     print("* " + "  " * 8 + "*")

# # Bottom of roof
# for j in range(10):
#     print("* ", end="")
# print()

# # House body with door
# for i in range(6):
#     for j in range(18):
#         if j == 0 or j == 4 or j == 17:
#             print("* ", end="")
#         elif 9 <= j <= 11 and i >= 2:
#             if j == 9 or j == 11 or (i == 2 and j == 10):
#                 print("* ", end="")
#             else:
#                 print("  ", end="")
#         else:
#             print("  ", end="")
#     print()

# # Bottom
# for j in range(18):
#     print("* ", end="")
# print()


def print_hut(width=25, wall_height=6, door_height=3, door_gap=3):
    """
    Prints an ASCII hut using only loops.
    width       : total width of the hut (must be odd for symmetry)
    wall_height : number of rows for the walls (including door row area)
    door_height : how tall the door slits are
    door_gap    : space between the two door lines
    """

    if width % 2 == 0:
        width += 1  # keep it odd for a symmetric peak

    mid = width // 2

    # 1. Roof (triangle) -------------------------------------------------
    for row in range(mid + 1):
        line = ""
        for col in range(width):
            # distance of this column from the center
            dist = abs(col - mid)
            if dist <= row:
                line += "*"
            else:
                line += " "
        print(line)

    # 2. Walls (hollow rectangle, full-width top border already drawn) ---
    for row in range(wall_height):
        line = ""
        for col in range(width):
            if col == 0 or col == width - 1:
                line += "*"          # left & right wall
            else:
                line += " "
        print(line)

    # 3. Bottom border with a door cut into it ---------------------------
    door_start = mid - (door_gap // 2) - 1
    door_end = mid + (door_gap // 2) + 1

    # door frame rows (two vertical strokes)
    for row in range(door_height):
        line = ""
        for col in range(width):
            if col == 0 or col == width - 1:
                line += "*"                      # outer walls
            elif col == door_start or col == door_end:
                line += "*"                      # door side posts
            else:
                line += " "
        print(line)

    # final bottom line (full border)
    line = ""
    for col in range(width):
        line += "*"
    print(line)


if __name__ == "__main__":
    print_hut(width=25, wall_height=6, door_height=3, door_gap=3)