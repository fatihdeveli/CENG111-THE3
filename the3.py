def place_words(corpus):
    def check(grd, corp):
        """
        Function checks if the word placements on a grid are valid according to the given corpus. Incomplete
        placements are valid placements.
        :param grd: List representing the grid: [row1, row2, ...]
        :param corp: Corpus
        :return: Boolean: True if there is no error with the placement, False otherwise.
        """
        normal_grid = grd
        grd = map(list, zip(*grd))  # Take the transpose of grid to check columns as words
        matching_words = 0
        for g_word in grd:  # Check every column with the words in corpus.
            for c_word in corp:
                if c_word.startswith(''.join(g_word)) and c_word not in normal_grid:
                    matching_words += 1
        return matching_words >= len(corp[0])

    for i, word in enumerate(corpus):  # Convert the words to uppercase
        corpus[i] = word.upper()

    grid_size = len(corpus[0])  # Length of words define the grid size
    grid = []
    checked_words = []
    for i in range(0, grid_size):
        checked_words.append([])
    '''
    checked_words keeps track of the words placed to grid for each row. A row is deleted if backtracked.
    checked_words = [
    ["ABC"]         --> Checked words for 1st row
    ["XYZ", "PQR"]  --> Checked words for 2nd row
    [...]]          --> ...
    '''

    while True:  # Loop through the words in the corpus to fill the grid. Loop ends if backtrack is needed.
        for word in corpus:
            if word not in grid and word not in checked_words[len(grid)]:
                grid.append(word)
                checked_words[len(grid) - 1].append(word)
                if check(grid, corpus):  # Check if the current grid is valid.
                    if grid_size == len(grid):  # Check if the grid is filled.
                        return grid
                else:
                    grid.pop()
        if len(checked_words[len(grid)]) + len(grid) == len(corpus):  # Backtrack
            if not grid:
                return False
            grid.pop()
            checked_words[len(grid)+1] = []


def main():
    print(place_words(["ALI", "SIN", "ASI", "LIR", "IRI", "INI", "KAR"]))


if __name__ == '__main__':
    main()
