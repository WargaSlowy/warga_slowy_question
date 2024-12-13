import unittest


from soal.soal_pertama import SolveItSoalPertama


if __name__ == "__main__":
    testing_soal_list: list = [SolveItSoalPertama]

    all_tests = unittest.TestSuite()
    for testing_semua in testing_soal_list:
        all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(testing_semua))
    unittest.TextTestRunner(verbosity=2).run(all_tests)
