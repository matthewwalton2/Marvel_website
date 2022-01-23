<!--- This script handles user input once they have selected a gender and a year --->
<?php

$serverName 	= "localhost";
$dbName 	= "mwalton2";
$user		= "mwalton2";
$pw	 	= "Oberlin@123";

function PrintPage($result_body, $query) {
  print("<!DOCTYPE html>\n
          <html>\n
            <head>\n
              <link rel='stylesheet' href='resultsStyle.css'>
              <title>Search Results</title>\n
            </head>\n
            <h1>\n
              Search Results <br>
            </h1>\n
            <h2>\n
              $query <br>
              $result_body <br>
            </h2>\n
            <h3>\n
              $result_body <br>
            </h3>\n
          </html>\n");
}


try {
    $firstInput = $_POST["firstTextInput"];
    $secondInput = $_POST["secondTextInput"];
    $thirdInput = $_POST["thirdTextInput"];
}
catch(PDOException $e) {
  PrintPage("Connection failed: " . $e->getMessage(), "Unknown");
}

  $result_body = "<table><tr><th>CharID</th><th>charName</th><th>Gender</th><th>eyeColor</th></tr>";

$conn = new PDO("mysql:host=$serverName;dbname=$dbName", 
    $user, $pw);
// set the PDO error mode to exception
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$query = 'select * from Characters where ' . $secondInput . ' = \'' . $thirdInput . '\';';
$stmt = $conn->prepare($query);
$stmt->execute();

foreach($stmt->fetchAll(PDO::FETCH_ASSOC) as $key => $val ) { 
  $result_body .= "<td>" . 
      $val['CharID'] . 
      "</td><td>" .
      $val['charName'] . 
      "</td><td>" .
      $val['Gender'] . 
      "</td><td>" . 
      $val['eyeColor'] . 
      "</td></tr>\n";
}
$result_body .= "</table>\n";

// Given statement
foreach($stmt->fetchAll(PDO::FETCH_ASSOC) as $key =>$val ) { 
  $result_body .= "<tr><td>$key</td><td>" . 
      $val['CharID'] . 
    "</td><td>" .
      $val['charName'] . 
    "</td><td>" .
      $val['Gender'] . 
    "</td><td>" .
      $val['eyeColor'] . 
      "</td></tr>\n";
  }
$result_body .= "</table>\n";
PrintPage($result_body, $query);

$conn = null;

?>