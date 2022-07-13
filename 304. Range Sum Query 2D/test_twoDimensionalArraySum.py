from twoDimensionalArraySum import NumMatrix

def test_1():
    numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    assert numMatrix.sumRegion(2, 1, 4, 3) == 8
    assert numMatrix.sumRegion(1, 1, 2, 2) == 11
    assert numMatrix.sumRegion(1, 2, 2, 4) == 12