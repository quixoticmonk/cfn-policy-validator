from aws_cdk import App, Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_sqs as sqs
from cdklabs.cdk_validator_cfnguard import CfnGuardValidator
from constructs import Construct


class DemoStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3.Bucket(self,"demo-bucket",
                  encryption=s3.BucketEncryption.S3_MANAGED)

        sqs.Queue(self, "demo-queue")

        Stack(
            self,
            "demo-stack",
        )


app = App(
    policy_validation_beta1=[
        CfnGuardValidator(control_tower_rules_enabled=True,rules=["./checks/sqs_encryption.guard"])
    ])
DemoStack(app, "demo-app")
app.synth()
