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
        operation, first, second
    )
    result = ops[operation](first, second)
    if result > 100:
        result = result * 2
        body += "Result: {} Due to the result is greater than 100, it's multiplied by 2<br>\n".format(
            result
        )
    elif result < 0:
        result = result + 50
        body += (
            "Result: {} Due to the result is less than 0, it's added by 50<br>\n".format(
                result
            )
        )
    else:
        body += "Result: {}<br>\n".format(result)

html = "<html>\n<head>\n<title>Mid term</title>\n</head>\n<body>\n"
url = "http://checkip.amazonaws.com"

with urllib.request.urlopen(url) as response:
    public_ip = response.read().decode("utf-8")

html += (
    body
    + "This result was processed on my EC2 instance with Public IP: {}<br>\nAccess the application via Load Balancer URL: http://WebServer-LB-1521782463.us-east-1.elb.amazonaws.com/math_form.php\n<br>\n".format(
        public_ip
    )
)
print(html)
