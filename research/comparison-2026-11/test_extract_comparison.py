import importlib.util
import pathlib
import unittest

PATH = pathlib.Path(__file__).with_name('extract_comparison.py')
spec = importlib.util.spec_from_file_location('extract_comparison', PATH)
extract = importlib.util.module_from_spec(spec)
spec.loader.exec_module(extract)

class ExtractionTests(unittest.TestCase):
    def test_identity_matching_requires_effort(self):
        rows = [{'name': 'Claude Sonnet 5.5', 'effort': 'max'}, {'name': 'Claude Sonnet 5.5 (xhigh)', 'effort': 'xhigh'}]
        self.assertIsNone(extract.find_row(rows, 'Claude Sonnet 5.5', 'medium'))
        self.assertEqual(extract.find_row(rows, 'Claude Sonnet 5.5', 'max'), rows[0])

    def test_complete_extraction_and_what_if(self):
        data = extract.build()
        self.assertEqual(len(data['configurations']), 9)
        self.assertEqual(sum('common' in c['tracks'] for c in data['configurations']), 7)
        self.assertEqual(data['whatIf']['common']['go']['multiple'], 10.0)
        self.assertAlmostEqual(data['whatIf']['main']['go']['costUsd'], 53.1435636733)
        self.assertLess(data['whatIf']['common']['go']['rank'], data['whatIf']['common']['publishedFallback']['rank'])
        self.assertEqual(len(data['pareto']['apiCommon']), 7)
        self.assertEqual(len(data['pareto']['planCommonWhatIf']), 7)

if __name__ == '__main__': unittest.main()
