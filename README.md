Based on the requirements, here are the core classes, functions, and methods that will be necessary:

1. `AWSClient` class:
   - Purpose: This class will handle the communication with the AWS API to retrieve pricing information.
   - Methods:
     - `get_instance_pricing(instance_type: str, region: str) -> float`: Retrieves the pricing for a specific instance type in a given region.
     - `get_bucket_pricing(region: str) -> float`: Retrieves the pricing for an S3 bucket in a given region.

2. `CostPredictor` class:
   - Purpose: This class will handle the prediction of costs based on the provided details.
   - Methods:
     - `predict_rds_cost(start_date: datetime, end_date: datetime, region: str, instance_type: str) -> float`: Predicts the cost of an RDS instance based on the start date, end date, region, and instance type.
     - `predict_instance_cost(start_date: datetime, end_date: datetime, region: str, instance_type: str) -> float`: Predicts the cost of an EC2 instance based on the start date, end date, region, and instance type.
     - `predict_bucket_cost(region: str) -> float`: Predicts the cost of an S3 bucket based on the region.

3. `Dashboard` class:
   - Purpose: This class will handle the GUI dashboard functionality.
   - Methods:
     - `display()`: Displays the GUI dashboard.

Now, let's proceed with creating the necessary files and implementing the code.

**aws_client.py**
