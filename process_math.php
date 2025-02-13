<?php
$first = $_POST['first'];
$second = $_POST['second'];
$operation = $_POST['operation'];
$command = escapeshellcmd("python3 math_operations.py $first $second \"$operation\"");
$output = shell_exec($command);
echo $output;
?>