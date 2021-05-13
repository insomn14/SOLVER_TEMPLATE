<?php
  require "flag.php";

  if(isset($_GET["text"])) {
    $text = $_GET["text"];
  }

  if (isset($_GET["text"])) {
    if ($text == "bruh") {
      if ($text == 0) {
        echo "<p>" . htmlentities($flag) . "</p>";
      }
    } else {
      echo "<p>bruh: wrong!</p>";
    }
  }

  if(isset($_GET["source"])) {
    echo "<pre>" .  htmlentities(file_get_contents("index.php", true)) . "</pre>";
  } else {
    echo "<!-- Source Code: ?source -->";
  }

?>
