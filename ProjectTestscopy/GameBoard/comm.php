<?php

require "../GameBoard/socket_client.php";

$q = $_REQUEST["q"];

$host    = "127.0.0.1";
$port    = 10236;
$message = $q;

$result = send2($host, $port, $message);

echo $result;




?>