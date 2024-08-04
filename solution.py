def traverse(mat, i, j, sum, path_sums):
    sum += mat[i][j]
    if i == len(mat) - 1 and j == len(mat[0]) - 1:
        path_sums.append(sum)
        return
    
    if i < len(mat) - 1:
        traverse(mat, i + 1, j, sum, path_sums)
    if j < len(mat[0]) - 1:
        traverse(mat, i, j + 1, sum, path_sums)
    
def solution(mat):
    path_sums = []
    traverse(mat, 0, 0, 0, path_sums)
    return max(path_sums)

if __name__ == "__main__":
    mat_1 = [[0, 3, 1 ,1], [2, 0, 0, 4], [1, 5, 3, 1]]
    mat_2 = [[0, 3, 1 ,1], [2, 9, 0, 4], [1, 5, 3, 1]]
    
    print(solution(mat_1))
    print(solution(mat_2))

    assert solution(mat_1) == 12
    assert solution(mat_2) == 21