from bs4 import BeatifulSoup

html_doc = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
     <p class = "title story title2"><b>The Dormouse's story</b></p> 
    <p class ="story">
      Once unpon a time here were three little sisters; and their namens were
      <a href="http://example.com/elsie" class="sister" id="Link1">Elsie</a>,
      <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
      and they lived at the bottom of a well.   
    </p>  
    <p>class="story"...</p>
    </body>
</html>
"""

contenido = BeatifulSoup{html_doc, "html_parser"}


