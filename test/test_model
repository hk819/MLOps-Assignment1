import unittest
import joblib

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        self.model = joblib.load('model/iris_model.pkl')  # Adjust the path as necessary

    def test_model_prediction(self):
        example_features = [[5.9, 3.0, 5.1, 1.8]]
        prediction = self.model.predict(example_features)
        self.assertIn(prediction[0], [0, 1, 2])

if __name__ == '__main__':
    unittest.main()