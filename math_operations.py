import boto3
import operator
import sys
import urllib.request

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

_, first, second, operation = sys.argv

first = float(first)
second = float(second)
body = ""
if second == 0 and operation == "/":
    body += "<p style='color: red;'>Division by zero is not allowed</p>\n"
else:
    body += "Operation: {}\n<br>\nInput 1: {}\n<br>\nInput 2: {}\n<br>\n".format(
        operation
    )
    result = ops[operation](first, second)
    if result > 100:
        result = result * 2
        body += "Result: {} Due to the result is greater than 100, it's multiplied by 2\n".format(
            result
        )
    elif result < 0:
        result = result + 50
        body += (
            "Result: {} Due to the result is less than 0, it's added by 50\n".format(
                result
            )
        )
    else:
        body += "Result: {}\n".format(result)

html = "<html>\n<head>\n<title>Mid term</title>\n</head>\n<body>\n"
ec2_client = boto3.client("ec2")
elb_client = boto3.client("elbv2")
url = "http://169.254.169.254/latest/meta-data/instance-id"
instance_id = urllib.request.urlopen(url).read().decode("utf-8")
ec2_response = ec2_client.describe_instances(InstanceIds=[instance_id])
public_ip = ec2_response["Reservations"][0]["Instances"][0].get("PublicIpAddress", None)
elb_response = elb_client.describe_load_balancers()
elb_url = ""
for lb in elb_response["LoadBalancerDescriptions"]:
    for instance in lb.get("Instances", []):
        if instance.get("InstanceId") == instance_id:
            elb_url = lb["DNSName"]
html += "This result was processed on my EC2 instance with Public IP: {}\n<br>\nAccess the application via Load Balancer URL: {}/math_form.php\n<br>\n".format(
    public_ip, elb_url
)

html += body + "</body>\n</html>"
print(html)
