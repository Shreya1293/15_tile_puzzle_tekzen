import unittest
from main import app, is_solvable


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"15 Tile Puzzle Game", response.data)

    def test_generate_puzzle(self):
        response = self.app.get("/generate-puzzle")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("puzzle", data)
        self.assertEqual(len(data["puzzle"]), 16)
        self.assertTrue(is_solvable(data["puzzle"]))

    def test_is_solvable(self):
        solvable_puzzle = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0
        ]
        unsolvable_puzzle = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0
        ]

        self.assertTrue(is_solvable(solvable_puzzle))
        self.assertFalse(is_solvable(unsolvable_puzzle))

    def test_static_files(self):
        with self.app.get("/static/styles.css") as response_css:
            self.assertEqual(response_css.status_code, 200)
            self.assertTrue(response_css.data)  #content shouldnt be empty

        with self.app.get("/static/script.js") as response_js:
            self.assertEqual(response_js.status_code, 200)
            self.assertTrue(response_js.data)  #shouldnt be empty


if __name__ == "__main__":
    unittest.main()