import unittest
from exchange import *


class TestLesson4(unittest.TestCase):
    def test_task_1(self):
        input_data = [(100000, 0.84), (700000, 10.1)]
        output_data = [119047, 69306]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(int(exchange_money(input_data[0], input_data[1])), output_data)

    def test_task_2(self):
        input_data = [(463000, 5000), (1250, 120), (15000, 1380)]
        output_data = [458000, 1130, 13620]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(get_change(input_data[0], input_data[1]), output_data)

    def test_task_3(self):
        input_data = [(10000, 128), (50, 360), (200, 200)]
        output_data = [1280000, 18000, 40000]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(get_value_of_bills(input_data[0], input_data[1]), output_data)

    def test_task_4(self):
        input_data = [(163270, 50000), (54361, 1000)]
        output_data = [3, 54]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(get_number_of_bills(input_data[0], input_data[1]), output_data)

    def test_task_5(self):
        inputs = [(100000, 10.61, 10, 1),
                  (1500, 0.84, 25, 40),
                  (470000, 1050, 30, 10000000000),
                  (470000, 0.00000009, 30, 700),
                  (425.33, 0.0009, 30, 700)]
        output_data = [8568, 1400, 0, 4017094016600, 363300]

        for variant, (inputs, output_data) in enumerate(zip(inputs, output_data), start=1):
            with self.subTest(f"variation #{variant}", inputs=inputs, output_data=output_data):
                self.assertEqual(exchangeable_value(inputs[0], inputs[1], inputs[2], inputs[3]), output_data)

    def test_task_6(self):
        inputs = [(100000, 10.61, 10, 1),
                  (1500, 0.84, 25, 40),
                  (425.33, 0.0009, 30, 700),
                  (12000, 0.0096, 10, 50)]
        output_data = [0, 28, 229, 13]

        for variant, (inputs, output_data) in enumerate(zip(inputs, output_data), start=1):
            with self.subTest(f"variation #{variant}", inputs=inputs, output_data=output_data):
                self.assertEqual(non_exchangeable_value(inputs[0], inputs[1], inputs[2], inputs[3]), output_data)


if __name__ == "__main__":
    unittest.main()
