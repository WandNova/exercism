import unittest
from arcade_game import *

class TestLesson3(unittest.TestCase):
    def test_task_1(self):
        power_data = [True, True, False, False]
        touching_data = [True, False, True, False]
        result_data = [True, False, False, False]
        for variant, (power_pellet_active, touching_ghost, result) in enumerate(zip(power_data, touching_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', power_pellet_active=power_pellet_active, touching_ghost=touching_ghost, result=result):
                failure_msg = f'Expected: {result} but the eat gost was calculated incorrectly.'
                self.assertEqual(eat_ghost(power_pellet_active, touching_ghost), result, msg=failure_msg)
 
    def test_task_2(self):
        touching_power_data = [True, True, False, False]
        touching_dot_data = [True, False, True, False]
        result_data = [True, True, True, False]
        for variant, (touching_power_pellet, touching_dot, result) in enumerate(zip(touching_power_data, touching_dot_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', touching_power_pellet=touching_power_pellet, touching_dot=touching_dot, result=result):
                failure_msg = f'Expected: {result} but the score was calculated incorrectly.'
                self.assertEqual(score(touching_power_pellet, touching_dot), result, msg=failure_msg)
                
    def test_task_3(self):
        power_data = [True, True, False, False]
        touching_data = [True, False, True, False]
        result_data = [False, False, True, False]
        for variant, (power_pellet_active, touching_ghost, result) in enumerate(zip(power_data, touching_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', power_pellet_active=power_pellet_active, touching_ghost=touching_ghost, result=result):
                failure_msg = f'Expected: {result} but the lose was calculated incorrectly.'
                self.assertEqual(lose(power_pellet_active, touching_ghost), result, msg=failure_msg)
                
    def test_task_4(self):
        all_dots_data = [True, False, True, True]
        power_data = [False, True, False, True]
        touching_data = [True, True, False, True]
        result_data = [False, False, True, True]
        for variant, (has_eaten_all_dots, power_pellet_active, touching_ghost, result) in enumerate(zip(all_dots_data, power_data, touching_data, result_data), start=1):
            with self.subTest(f'variation #{variant}',has_eaten_all_dots=has_eaten_all_dots, power_pellet_active=power_pellet_active, touching_ghost=touching_ghost, result=result):
                failure_msg = f'Expected: {result} but the win was calculated incorrectly.'
                self.assertEqual(win(has_eaten_all_dots, power_pellet_active, touching_ghost), result, msg=failure_msg)
if __name__ == "__main__":
    unittest.main()
