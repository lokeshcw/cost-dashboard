from aws_client import AWSClient
from cost_predictor import CostPredictor
from dashboard import Dashboard

aws_client = AWSClient()
cost_predictor = CostPredictor(aws_client)
dashboard = Dashboard(cost_predictor)

dashboard.display()
