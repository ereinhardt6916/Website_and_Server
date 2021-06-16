var turn = 0; 
var mycolour = "black"; 
var opcolour = "white";
var response;
var strlen;
var numMess;
var i;
var command; 
//&& )

function addPiece(loc){
    //turn = localStorage.getItem("turn");
    document.getElementById("txtHint").innerHTML = "123456";//show what the server sent back

    if(document.getElementById(loc).className == "empty" || document.getElementById(loc).className == "but") {
        if(turn == 0)
        {
       
            if(loc == "Skip" || loc == "!surr"){

            }
            else{
                document.getElementById(loc).className = mycolour; 
            }

            turn = 1;
            document.getElementById("txtHint").innerHTML = turn;//show what the server sent back

            document.getElementById("turn").innerHTML = opcolour;
            
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    response = this.responseText;

                    //document.getElementById("txtHint").innerHTML = response;//show what the server sent back
                    
                    strlen = response.length;
                    numMess = strlen/4; //find out how many messages there are

                    for (let i = 0; i < numMess; i++) {
                        command = response.slice(i*4,(i*4)+4);
        
                        if(command[0] == 'A'){
                            command = command.slice(1,4);
                            document.getElementById(command).className = opcolour; //add opponents piece
                        }
                        else if(command[0] == 'R'){
                            command = command.slice(1,4);
                            document.getElementById(command).className = "empty"; //add opponents piece
                        }
                        else if(command == 'Skip'){
                            //oponent decides not to play their turn
                        }
                        else if(command == '!sur'){
                            //oponent decides 
                            window.location.href = "../GameBoard/GameOver.php";

                        }
                        else if(command[0] == 'W'){
                            whiteScore = command.slice(2,4);
                            document.getElementById("whiteScore").innerHTML = whiteScore;
                        } 
                        else if(command[0] == 'B'){
                            blackScore = command.slice(2,4);
                            document.getElementById("blackScore").innerHTML = blackScore;
        
                        }                    
                    }
                    if(turn == 1){
                        turn = 3;
                        //this one went first
                    }
                    else if(turn == 2){
                        turn = 0; 
                        //this one went second
                    }
                    
                    sendVoid();

                }
            };
            xmlhttp.open("GET", "comm.php?q=" + loc, true);
            xmlhttp.send();


        }
    }
}

function sendVoid(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = this.responseText;

            document.getElementById("txtHint").innerHTML = response;//show what the server sent back
            
            strlen = response.length;
            numMess = strlen/4; //find out how many messages there are

            for (let i = 0; i < numMess; i++) {
                command = response.slice(i*4,(i*4)+4);

                if(command[0] == 'A'){
                    command = command.slice(1,4);
                    document.getElementById(command).className = opcolour; //add opponents piece
                }
                else if(command[0] == 'R'){
                    command = command.slice(1,4);
                    document.getElementById(command).className = "empty"; //add opponents piece
                }
                else if(command == 'Skip'){
                    //oponent decides not to play their turn
                }
                else if(command[0] == '!'){
                    //oponent decides 
                    document.getElementById("blackScore").innerHTML = "worked!!!";
                    window.location.href = "../GameBoard/GameOver.php";

                }
                else if(command[0] == 'W'){
                    whiteScore = command.slice(2,4);
                    document.getElementById("whiteScore").innerHTML = whiteScore;
                } 
                else if(command[0] == 'B'){
                    blackScore = command.slice(2,4);
                    document.getElementById("blackScore").innerHTML = blackScore;

                }                    
            }
            document.getElementById("turn").innerHTML = mycolour;
            if(turn == 1){
                turn = 2;
                //This one went first
            }
            else if(turn = 3){
                turn = 0;
                //other one went first
            }

        }
       
    };
    xmlhttp.open("GET", "comm.php?q=" + "void", true);
    xmlhttp.send();
}

var myColourChoice = "Whit"; //if user doesn't select, defaults to black

//function to run when the user enters in the needed data
function startUp(){
    document.getElementById("abc").innerHTML = "went to start function";//show what the server sent back

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = this.responseText;
            document.getElementById("abc").innerHTML = response;//show what the server sent back

            
            strlen = response.length;
            numMess = strlen/4; //find out how many messages there are

            for (let i = 0; i < numMess; i++) {
                command = response.slice(i*4,(i*4)+4);

                if(command[0] == 'W'){
                    mycolour = "white";
                    opcolour = "black";
                    document.getElementById("abc").innerHTML = mycolour;//show what the server sent back
                    localStorage.setItem("mycolour", mycolour);
                    localStorage.setItem("opcolour", opcolour);

                }
                else if(command[0] == 'B'){
                    mycolour = "black";
                    opcolour = "white";
                    document.getElementById("abc").innerHTML = mycolour;//show what the server sent back
                    localStorage.setItem("mycolour", mycolour);
                    localStorage.setItem("opcolour", opcolour);
                }
                else if(command[0] == '0'){
                    turn = 0; //it is my turn to go
                    localStorage.setItem("turn", "0");

                }
                else if(command[0] == '1'){
                    turn = 1; //it is not my turn
                    localStorage.setItem("turn", "1");

                }
                          
            }
            window.location.href = "../GameBoard/BoardTest.php";

        }
    };
    xmlhttp.open("GET", "StartUp.php?q=" + myColourChoice, true);
    xmlhttp.send();

  // document.getElementById("abc").innerHTML = localStorage.getItem("turn");//show what the server sent back



}

function setMyColour(choice){

    if(choice == "white"){
        myColourChoice = "Whit";
        document.getElementById("abc").innerHTML = myColourChoice;//show what the server sent back

    }
    else if(choice == "black"){
        myColourChoice = "Blac"
        document.getElementById("abc").innerHTML = myColourChoice;//show what the server sent back

    }
}

//runs when the game board page is loaded to initalize the values
function onLoad(){
    mycolour = localStorage.getItem("mycolour");
    opcolour = localStorage.getItem("opcolour");
    turn = localStorage.getItem("turn");

    if (turn == "1"){
        //if I do not go first
        turn = 3;
        sendVoid(); 
    }
}

function gameOver(){

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = this.responseText;

            
            strlen = response.length;
            numMess = strlen/4; //find out how many messages there are

            for (let i = 0; i < numMess; i++) {
                command = response.slice(i*4,(i*4)+4);

                if(command[0] == 'W'){
                    whiteScore = command.slice(2,4);
                    document.getElementById("whiteScoreEnd").innerHTML = whiteScore;
                } 
                else if(command[0] == 'B'){
                    blackScore = command.slice(2,4);
                    document.getElementById("blackScoreEnd").innerHTML = blackScore;

                }                    
            }

            if(whiteScore > blackScore){
                //white won
                document.getElementById("winner").innerHTML = "White Won!";

            }
            else{
                //Black
                document.getElementById("winner").innerHTML = "Black Won!";
            }

        }
       
    };
    xmlhttp.open("GET", "comm.php?q=" + "WINR", true);
    xmlhttp.send();
}





