#!/bin/unknown
# should not report SC1008, SC2140 
# should report SC1098
echo "<img src="foo.png" />" > file.html
eval $var=(a b)