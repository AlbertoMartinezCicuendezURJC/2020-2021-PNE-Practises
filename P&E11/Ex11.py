import cv2
import numpy as np

initial_image = cv2.imread('noisy_radiography.png', 0)
m, n = initial_image.shape
filtered_image = np.zeros([m, n])

# Loop 'for' to change pixels in the first row

cte_row = 0
for column2 in range(0, n - 1):
    if column2 == 0:
        original_matrix2 = [initial_image[cte_row + 1, column2], initial_image[cte_row + 1, column2 + 1], initial_image[cte_row, column2 + 1], initial_image[cte_row, column2]]
        minimum2 = min(original_matrix2)
        filtered_image[cte_row, column2] = minimum2

    elif column2 == n - 1:
        original_matrix3 = [initial_image[cte_row , column2 - 1], initial_image[cte_row, column2], initial_image[cte_row + 1, column2 - 1], initial_image[cte_row + 1, column2]]
        minimum3 = min(original_matrix3)
        filtered_image[cte_row, column2] = minimum3

    else:
        original_matrix4 = [initial_image[cte_row, column2 - 1], initial_image[cte_row, column2], initial_image[cte_row, column2 + 1], initial_image[cte_row + 1, column2 - 1], initial_image[cte_row + 1, column2], initial_image[cte_row + 1, column2 + 1]]
        minimum4 = min(original_matrix4)
        filtered_image[cte_row, column2] = minimum4



# Loop 'for' to change pixels in the last row

cte_row2 = m - 1
for column3 in range(0, n - 1):
    if column3 == 0:
        original_matrix7 = [initial_image[cte_row2 - 1, column3], initial_image[cte_row2, column3], initial_image[cte_row2 - 1 , column3 + 1], initial_image[cte_row2, column3 + 1]]
        minimum7 = min(original_matrix7)
        filtered_image[cte_row2, column3] = minimum7

    elif column3 == n - 1:
        original_matrix3 = [initial_image[cte_row2 , column3 - 1], initial_image[cte_row2, column3], initial_image[cte_row2 -1, column3 - 1], initial_image[cte_row2 - 1, column3]]
        minimum3 = min(original_matrix3)
        filtered_image[cte_row2, column3] = minimum3

    else:
        original_matrix4 = [initial_image[cte_row2, column3 - 1], initial_image[cte_row2, column3], initial_image[cte_row2, column3 + 1], initial_image[cte_row2 - 1, column3 - 1], initial_image[cte_row2 - 1, column3], initial_image[cte_row2 - 1, column3 + 1]]
        minimum4 = min(original_matrix4)
        filtered_image[cte_row2, column3] = minimum4


# Loop 'for' to change pixels in the first column

cte_column = 0
for row in range(1, m - 1):
    original_matrix5 = [initial_image[row, cte_column], initial_image[row, cte_column + 1], initial_image[row + 1, cte_column], initial_image[row + 1, cte_column + 1], initial_image[row - 1, cte_column], initial_image[row - 1, cte_column + 1]]
    minimum5 = min(original_matrix5)
    filtered_image[row, cte_column] = minimum5


# Loop 'for' to change pixels in the last column

cte_column = n - 1
for row in range(1, m - 1):
    original_matrix6 = [initial_image[row, cte_column], initial_image[row, cte_column - 1], initial_image[row + 1, cte_column], initial_image[row + 1, cte_column - 1], initial_image[row - 1, cte_column], initial_image[row - 1, cte_column - 1]]
    minimum6 = min(original_matrix6)
    filtered_image[row, cte_column] = minimum6


# Loops 'for' to change pixels that not belong to the borders

for row in range(1, m - 1):
    for column in range(1, n - 1):
        original_matrix = [initial_image[row - 1, column - 1], initial_image[row - 1, column], initial_image[row - 1, column + 1],
                           initial_image[row, column - 1], initial_image[row, column], initial_image[row, column + 1],
                           initial_image[row + 1, column - 1], initial_image[row + 1, column], initial_image[row + 1, column + 1]]

        minumum = min(original_matrix)
        filtered_image[row, column] = minumum


filtered_image = filtered_image.astype(np.uint8)
cv2.imshow('filtered_with_minimum.png', filtered_image)


cv2.waitKey(0)
cv2.destroyAllWindows()





