<?php
$document = "<html>
    <head>
        <title>Title of the document</title>
        // The HTML header comes here
    </head>
    <body>
        This is the body of the document
        It is usually several lines long
    </body>
    </html>";
 
if (preg_match("#<title>(.*)</title>#i",$document,$matches)) {
    echo "The title of the document is: " . $matches[1] . "\n";
}


?>
