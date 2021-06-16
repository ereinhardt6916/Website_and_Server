<?php
// set some variables
$i = 0;
$host = "127.0.0.1";
$port = 10231;

$mesg = ["1111,Whit","A9.9","W003B050","A1.1","R1.1W020B000","A2.2","W030","A3.3","R2.2","A1.1","R1.1!sur","void","W020B010"];

// don't timeout!
set_time_limit(0);
// create socket
$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
// bind socket to port
if(!socket_set_option($socket,SOL_SOCKET, SO_REUSEADDR,1)){
    echo socket_strerror(socket_last_error($socket));
    exit;
}
 $result = socket_bind($socket, $host, $port) or die("Could not bind to socket\n");

for($i = 0; $i<13; $i++){

    // start listening for connections
    $result = socket_listen($socket, 3) or die("Could not set up socket listener\n");

    // accept incoming connections
    // spawn another socket to handle communication
    $spawn = socket_accept($socket) or die("Could not accept incoming connection\n");
    // read client input
    $input = socket_read($spawn, 1024) or die("Could not read input\n");
    // clean up input string
    $input = trim($input);
    echo "Client Message : ".$input;
    
    sleep(1);
    // reverse client input and send back
    $output = $mesg[$i];
    echo "writing : ".$output;
    socket_write($spawn, $output, strlen ($output)) or die("Could not write output\n");


}




/*
// start listening for connections
$result = socket_listen($socket, 3) or die("Could not set up socket listener\n");
// accept incoming connections
// spawn another socket to handle communication
$spawn = socket_accept($socket) or die("Could not accept incoming connection\n");
// read client input
$input = socket_read($spawn, 1024) or die("Could not read input 1\n");
// clean up input string
$input = trim($input);
echo "Client Message : ".$input;

sleep(2);
// reverse client input and send back
$output = "A5.5A1.1W050B040";
echo "writing : ".$output;
socket_write($spawn, $output, strlen ($output)) or die("Could not write output\n");


*/

// close sockets
socket_close($spawn);
socket_close($socket);
?>