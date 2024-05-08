def get_knight_moves(start_position):
    row = int(start_position[1])
    column = ord(start_position[0]) - ord('a') + 1

    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    count = 0

    for move in moves:
        new_row = row + move[0]
        new_column = column + move[1]
        if 1 <= new_row <= 8 and 1 <= new_column <= 8:
            count += 1

    return count

# 입력 받기
input_data = input("Enter knight's position (e.g., 'b3'): ")
result = get_knight_moves(input_data)
print(result)
