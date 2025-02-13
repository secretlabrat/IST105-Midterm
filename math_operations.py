import operator
import sys

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

_, first, second, operation = sys.argv

first = float(first)
second = float(second)
body = ""
if second == 0 and operation == "/":
    body += "<p style='color: red;'>Division by zero is not allowed</p>\n"
else:
    body += "<p>Operation: {} {} {}</p>\n".format(first, operation, second)
    result = ops[operation](first, second)
    if result > 100:
        result = result * 2
        body += "<p>Result: {} Due to the result is greater than 100, it's multiplied by 2</p>\n".format(
            result
        )
    elif result < 0:
        result = result + 50
        body += "<p>Result: {} Due to the result is less than 0, it's added by 50</p>\n".format(
            result
        )
    else:
        body += "<p>Result: {}</p>\n".format(result)

html = "<html>\n<head>\n<title>Mid term</title>\n</head>\n<body>\n"
html += body + "</body>\n</html>"
print(html)
