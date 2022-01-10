<?php
$myfile = fopen("testfile1.txt", "w");
$name = $_POST['name']. "\n";
fwrite($myfile, $name);
$surname = " " . $_POST['surname'] . "\n";
fwrite($myfile, $surname);
$email = " " . $_POST['email'] . "\n";
fwrite($myfile, $email);
$feedback = " " . $_POST['feedback'] . "\n";
fwrite($myfile, $feedback);

fclose($myfile);

?>