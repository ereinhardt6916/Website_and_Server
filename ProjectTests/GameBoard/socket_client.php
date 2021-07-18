<?php


function send1($host, $port, $message){

    $socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
    // connect to server
    $result = socket_connect($socket, $host, $port) or die("Could not connect to server\n");  
    // send string to server
    socket_write($socket, $message, strlen($message)) or die("Could not send data to server\n");
    $result = socket_read ($socket, 1024) or die("Could not read server response\n");

    socket_close($socket);

    return $result; 
}

require_once('../Socket/shelper.php');

function send2($host, $port, $message){

    // connect to server
    $sockethelper = new sockethelper($host,$port);
    
    // send string to server
    $sockethelper->send_data($message);
    
    //read data from server
    $result = $sockethelper->read_data();
    
    //close the socket
    $sockethelper->close_socket();

    return $result; 
}

?>