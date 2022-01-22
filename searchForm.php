<!--- This script handles user input once they have selected a gender and a year --->
<?php

$serverName 	= "localhost";
$dbName 	= "movies";
$user		= "mwalton2";
$pw	 	= "Oberlin@123";

function PrintPage($body, $year) {
  print("<!DOCTYPE html>\n");
  print("<html>\n<head>\n<title>This is the movie handler!</title>\n");
  print("</head>\n<body>\n");
  
  print("<h1>Top movies from $year</h1>\n");
  
  print("<div class='formOutput'>$body\n</div>\n");
  
  print("</body>\n</html>\n");
}


try {
    $selectedRadio = $_POST["GenderRadio"];
    $userYear = $_POST["TextYear"];
    echo "You selected: $selectedRadio from the year $userYear";

  $year = $_POST['year'];
  //  $year = "1995; delete from students;";

  $body = "<table><tr><th>ID</th><th>Title</th><th>Average Rating</th></tr>";

  $conn = new PDO("mysql:host=$serverName;dbname=$dbName", 
		  $user, $pw);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

  // Test statement
  //$stmt = $conn->prepare('select title, year from movies limit 20;');
  
  
  // given statement:
  $stmt = $conn->prepare('select title, avg(rating) as avg_rating from movies natural join ratings WHERE YEAR = :year group by title order by avg_rating desc limit 20;');
                          
  $year = 1995;
  $stmt->execute( array(':year' => $year) );

  /*
  // Test: Change variable names to reflect sql query
  foreach($stmt->fetchAll(PDO::FETCH_ASSOC) as $key =>$val ) { 
    $body .= "<tr><td>$key</td><td>" . 
		   $val['title'] . 
		   "</td><td>" . $val['year'] . "</td></tr>\n";
  } */

  
  // Given statement
  foreach($stmt->fetchAll(PDO::FETCH_ASSOC) as $key =>$val ) { 
    $body .= "<tr><td>$key</td><td>" . 
		   $val['title'] . 
		   "</td><td>" . $val['avg_rating'] . "</td></tr>\n";
  }
  

  $body .= "</table>\n";

  PrintPage($body, $year);

}

catch(PDOException $e) {
  PrintPage("Connection failed: " . $e->getMessage(), "Unknown");
}


$conn = null;
?>