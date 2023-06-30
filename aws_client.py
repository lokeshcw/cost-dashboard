import boto3

class AWSClient:
    def __init__(self):
        self.pricing_client = boto3.client('pricing', region_name='us-east-1')

    def get_instance_pricing(self, instance_type: str, region: str) -> float:
        # Implement the logic to retrieve instance pricing from AWS API
        # Return the pricing for the specified instance type and region
        pass

    def get_bucket_pricing(self, region: str) -> float:
        # Implement the logic to retrieve bucket pricing from AWS API
        # Return the pricing for the specified region
        pass
