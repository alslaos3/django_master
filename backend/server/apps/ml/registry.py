from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints.models import MLAlgorithmStatus

class MLRegistry:
    def __init__(self):
        self.endpoints = {}

    def add_algorithm(self, endpoint_name, algorithm_object, algorithm_name, algorithm_status, algorithm_version,
                      owner, algorithm_description, algorithm_code):
        endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)
        # database_object = 생성된(get이나 created된) 객체, algorithm_created = 생성에 대한 Boolean (기존:0,새로:1)
        database_object, algorithm_created = MLAlgorithm.objects.get_or_create(
            name=algorithm_name,
            description=algorithm_description,
            code=algorithm_code,
            version=algorithm_version,
            owner=owner,
            parent_endpoint=endpoint)
        if algorithm_created :
            status = MLAlgorithmStatus(status = algorithm_status,
                                       created_by = owner,
                                       parent_mlalgorithm = database_object,
                                       active = True)
            status.save()

        self.endpoints[database_object.id] = algorithm_object