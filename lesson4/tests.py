import unittest
from exchange import *

class TestLesson4(unittest.TestCase):
    def test_task_1(self):
        inputs = [100000, 10.61, 10, 1]
        output_data = [8568, 1400, 0, 4017094016600, 363300]

        for variant, (inputs, output_data) in enumerate(zip(inputs, output_data), start=1):
            with self.subTest(f"variation #{variant}", inputs=inputs, output_data=output_data):
                failure_msg = f'Expected: {result} but the eat gost was calculated incorrectly.'
                self.assertEqual(exchangeable_value(inputs[0], inputs[1], inputs[2], inputs[3]), output_data)
if __name__ == "__main__":
    unittest.main()
