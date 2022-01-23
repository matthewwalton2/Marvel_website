<!--- This script handles user input once they have selected a gender and a year --->
<?php

$serverName 	= "localhost";
$dbName 	= "mwalton2";
$user		= "mwalton2";
$pw	 	= "Oberlin@123";

function PrintPage($result_header, $result_body, $query) {
  print("<!DOCTYPE html>\n
          <html>\n
            <head>\n
              <link rel='stylesheet' href='resultsStyle.css'>
              <title>Search Results</title>\n
            </head>\n
            <h1>\n
              Search Results <br>
            </h1>\n
            <h2 class=\"container\">\n
              <p1>\n
                $query <br>
              </p1>\n
              <p2>\n
                $result_header <br>
              </p2>\n
              <p3>\n
                $result_body <br>
              </p3>\n
            </h2>\n
          </html>\n");
}

try {
    $firstInput = $_POST["firstTextInput"];
    $secondInput = $_POST["secondTextInput"];
    $thirdInput = $_POST["thirdTextInput"];
    $comparator = $_POST["comparator"];
}
catch(PDOException $e) {
  PrintPage("Connection failed: " . $e->getMessage(), "Unknown");
}

$result_header = "<table><tr>
  <th>Name</th>
  <th>Affiliation</th>
  <th>Gender</th>
  <th>Height</th>
  <th>Weight</th>
  <th>Eyes</th>
  <th>Hair</th>
  <th>Origin</th>
  <th>Living Status</th>
  <th>Reality</th>
  <th>Birthplace</th>
  <th>Identity</th>
  <th>Citizenship</th>
  <th>Occupation</th>
  <th>Creator</th>
  <th>Premiere</th>
  </tr></table>";
$result_body = "<table>";

$conn = new PDO("mysql:host=$serverName;dbname=$dbName", 
    $user, $pw);
// set the PDO error mode to exception
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

if($comparator == 'R'){
  $query = 'select * from Characters where ' . $secondInput . ' ' . 'RLIKE' . ' \'' . $thirdInput . '\';';
}
else{
  $query = 'select * from Characters where ' . $secondInput . ' ' . $comparator . ' \'' . $thirdInput . '\';';
}

$stmt = $conn->prepare($query);
$stmt->execute();


foreach($stmt->fetchAll(PDO::FETCH_ASSOC) as $key => $val ) { 
  $result_body .= "<td>" . 
      //$val['ID'] . 
      //"</td><td>" .
      $val['Name'] . 
      "</td><td>" .
      $val['Affiliation'] . 
      "</td><td>" . 
      //$val['Marital Status'] . 
      //"</td><td>" .
      $val['Gender'] . 
      "</td><td>" .
      $val['Height'] . 
      "</td><td>" .
      $val['Weight'] . 
      "</td><td>" .
      $val['Eyes'] . 
      "</td><td>" .
      $val['Hair'] . 
      "</td><td>" .
      //$val['Unusual Features'] . 
      //"</td><td>" .
      $val['Origin'] . 
      "</td><td>" .
      $val['Living Status'] . 
      "</td><td>" .
      $val['Reality'] . 
      "</td><td>" .
      $val['Birthplace'] . 
      "</td><td>" .
      $val['Identity'] . 
      "</td><td>" .
      $val['Citizenship'] . 
      "</td><td>" .
      $val['Occupation'] . 
      "</td><td>" .
      $val['Creator'] . 
      "</td><td>" .
      //$val['Creatr'] . 
      //"</td><td>" .
      $val['Premiere'] . 
      "</td></tr>\n";
}
$result_body .= "</table>\n";

PrintPage($result_header, $result_body, $query);

$conn = null;

?>
