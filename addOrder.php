<?php
$hostname = "127.0.0.1";
$database = "delivery_database";
$table = "customer_table";
$username = "root";
$password = "";

$conn = mysqli_connect($hostname, $username, $password, $database);

if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
}
 
echo "Connected successfully<br>";
 

$name = $_POST['name'];
$surname =$_POST['surname'] ;
$patronymic = $_POST['patronymic'];
$address = $_POST['address'];
$phonenumber =  $_POST['phonenumber'];
$email = $_POST['email'];
$product= $_POST['productSelect'];
$comment =  $_POST['comment'] ;


$result=mysqli_query($conn,"SELECT count(*) as total from {$table}");
$id=mysqli_fetch_assoc($result);


$sql = "INSERT INTO $table (ID,name,surname,patronymic,address,phonenumber,email,product,comment ) 
VALUES ('{$id['total']}', '{$name}', '{$surname}', '{$patronymic}', '{$address}', '{$phonenumber}', '{$email}', '{$product}', '{$comment}')";
if (mysqli_query($conn, $sql)) {
      echo "New record created successfully";
} else {
      echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
mysqli_close($conn);
?>