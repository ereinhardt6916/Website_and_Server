<?php
session_start();
$username = $_POST['username'];
$password = $_POST['password'];

function verify_credential ($username, $password) :bool {

    //database parameters
    $db = new PDO(
        'mysql:host=127.0.0.1;dbname=go',
        'username',
        '1234'
    );

    //return arrays with keys that are the name of the fields
    $db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

    //prepare SQL statement
    $query = 'SELECT password FROM login WHERE username=:username;';
    $statement = $db->prepare($query);
    $statement->bindValue('username', $username);

    //execute the SQL statement and store return array at $row
    $result = $statement->execute();
    $row = $statement->fetchAll();

    //check execution result
    if (!$result){
        //execution failed
        return false;
    }else{
        //execution successfully
        //compare return password
        //since username is a primary key, the return 2-D array will only has one element
        if ($row == [])
            //no such username
            return false;
        else if ($row[0]['password'] == $password){
            //found username, password matched
            $authorized = $row[0]['authorized'];
            return true;
        }
        else
            //found username, password wrong
            return false;
    }
 

}

if(verify_credential($username, $password)){
    $_SESSION['username']=$username;
    require '../index/index.php';    
}
else{
    echo "Failed to enter";
    require "../login/login.php";
}
?>
