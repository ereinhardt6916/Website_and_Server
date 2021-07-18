<?php

$username = $_POST['username'];
$password =$_POST['password'];


//create new user array
$new_user = [
    "username" => $username,
    "password" => $password,
];

function createNewUser() :bool {
    global $new_user;

    //database parameters
    $db = new PDO(
        'mysql:host=127.0.0.1;dbname=go',
        'username',
        '1234'
    );

    //return arrays with keys that are the name of the fields
    $db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

    //create SQL statement
    $query = 'INSERT INTO login (username, password) VALUES (:username, :password)';

    //execute SQL statement at database
    $statement = $db->prepare($query);
    $result = $statement->execute($new_user);

    if($result)
        return true;
    else{
        $error2 = $statement->errorInfo();
        return false;
    }

}

require '../Navbar/bar_LO.html';

if(createNewUser())
{
    require '../login/login.html'; //take to login page   

}
else{

    require '../signup/signup.html'; //if fails loop back to req_access page
    require '../signup/req_aces_fail.html';
}
?>