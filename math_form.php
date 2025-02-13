<?php
$public_ip = file_get_contents('http://checkip.amazonaws.com');
?>
Welcome to the Mathematical Application!<br>
This application is hosted on my EC2 instance with Public IP: <?php echo $public_ip ?><br>
Enter two numbers and select an operation to calculate the result.<br>
<form action="process_math.php" method="POST">
Number 1: <input type="number" name="first"><br>
Number 2: <input type="number" name="second"><br>
Operation: <select name="operation">
    <option value="+">+</option>
    <option value="-">-</option>
    <option value="*">x</option>
    <option value="/">÷</option>
  </select>
  <br>
  <br>
<input type="submit" value="Calculate">
</form>