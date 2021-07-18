<?php
session_start();
if(isset($_SESSION['username'])){
    require "../Navbar/bar_LI.html";
}
else{
    require "../Navbar/bar_LO.html";
}
require "../index/index.html";

?>

