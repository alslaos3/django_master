from django.test import TestCase

from apps.ml.classifier.random_forest import RandomForestClassifier
import inspect
from apps.ml.registry import MLRegistry

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {"S1":0,	"S2":0.19444,	"S3":0.17222,	"S4":1.1088,	"S5":0.46765,
                      "S6":0.45294,	"S7":0.63542,	"S8":0.81944,	"S9":0.63542,	"S10":1.3706,
                      "S11":0.28235,	"S12":0.082353,	"S13":1.5455,	"S14":0.62273,	"S15":0.95909,
                      "S16":0.81197,	"S17":0.029915,	"S18":2.2094,	"S19":1.9415,	"S20":0,
                      "S21":0.035088,	"S22":0.11905,	"S23":1.4077,	"S24":0.39286,	"S25":0,
                      "S26":0.125,	"S27":2.1369,	"S28":0.61905,	"S29":1.0571,	"S30":0.72698,
                      "S31":1.3944,	"S32":0.066667,	"S33":0.78889,	"S34":0.81818,	"S35":1.9909,
                      "S36":0.49091,	"S37":1.2847,	"S38":0.72222,	"S39":0.70833,	"S40":1.1209,
                      "S41":1.7912,	"S42":0.73626,	"S43":1.1923,	"S44":0.72308,	"S45":0.21538,
                      "S46":0.51373,	"S47":0.098039,	"S48":0.1451,	"S49":0.83333,	"S50":1.2932,
                      "S51":0.5216,	"S52":0.49242,	"S53":0.068182,	"S54":0.64394,	"S55":0.87607,
                      "S56":0.75641,	"S57":1.2308,	"S58":0.87963,	"S59":0.12963,	"S60":2.1343}
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('Patient', response['label'])

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "endpoint_test"
        algorithm_object = RandomForestClassifier()
        algorithm_name = "test"
        algorithm_status = "testing"
        algorithm_version = "0.0.1"
        algorithm_owner = "Jeong Seok Han"
        algorithm_description = "endpoint test"
        algorithm_code = inspect.getsource(RandomForestClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                               algorithm_status, algorithm_version, algorithm_owner,
                               algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)