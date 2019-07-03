#!/usr/bin/env python3

import unittest
from src import matrix


class TestMatrix(unittest.TestCase):
    def _test_found_rectangles(self, given_matrix, expected_rectangles):
        mat = matrix.Matrix(given_matrix)
        rectangles = mat.find_rectangles()
        self.assertEqual(rectangles, expected_rectangles)

    def test_empty(self):
        mat = matrix.Matrix([])

        self.assertEqual(mat.cols, 0)
        self.assertEqual(mat.rows, 0)

        rectangles = mat.find_rectangles()
        self.assertEqual(rectangles, [0,0,0,0])


if __name__ == '__main__':
    unittest.main()
