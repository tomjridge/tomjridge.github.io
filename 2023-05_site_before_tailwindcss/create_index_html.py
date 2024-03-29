# import markdown

from shared import *

# https://realpython.com/python-f-strings/  .format(**record)

# @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap'); 
# @import url('https://fonts.googleapis.com/css2?family=PT+Serif&display=swap');

base_css="""
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

body {
  font-family: 'Roboto'; 
/* 'PT Serif' 'Roboto', arial, sans-serif Georgia, "Times New Roman", Times, serif; */
  color: #222;
  line-height: 1.5;
}

h1, .h1,
h2, .h2,
h3, .h3,
h4, .h4,
h5, .h5,
h6, .h6 {
  font-weight: bold;
  color: #333;
}

#content h1 {
    font-size: 38px;
    text-align:center;
}

a {
  color: #333;
}

span.trophy::before {
  content: "🏆"
}

"""

# social ---------------------------------------------------------------

# https://www.w3schools.com/howto/howto_css_social_media_buttons.asp
font_awesome_head="""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" crossorigin="anonymous" />
<style>
.fab, .fas {
  padding: 10px;
  font-size: 20px;
  width: 20px;
  height: 20px;
  text-align: center;
  text-decoration: none;
  border-radius: 50%;

  background: #3B5998;
  color: white;
}
</style>
"""

def social_fab(name,href):
    return f"""<span><a href="{href}" class="fab fa-{name}"></a></span>"""

def social_fas(name,href):
    return f"""<span><a href="{href}" class="fas fa-{name}"></a></span>"""

def social_university():
    return social_fas("university","https://scholar.google.com/citations?user=WYsimU8AAAAJ&hl=en")

#def social_text(s):
#    return f"""<span><a href="#" class="fab"><span style='font-size:15px'>{s}</span></a></span>"""

def social_bar():
    return f"""
    {social_fab("github","https://github.com/tomjridge")}
    {social_fab("mastodon","https://realscience.social/web/accounts/6589")}
    {social_university()}
    {social_fab("youtube","https://www.youtube.com/channel/UCDnseBjY0_sUzPvgFt38hug")}
    {social_fab("blogger","https://tom-ridge.blogspot.com/")}
"""

#    {social_fas("book","")}


# end social -----------------------------------------------------------


# navbar ---------------------------------------------------------------

navbar_css="""
.navbar {
  background-color: rgb(63,182,24);
  padding: 0.5em;
}

.navbar ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.navbar li {
  display: inline;
  margin: 0 0.2em;
}

.navbar a {
  font-family: sans-serif;
  font-weight: bold;
  color: white;
}
"""

navbar = """
<!-- navbar ---------------------------------------- -->

<div class='navbar'>
  <ul>
    <li><a href='index.html'>Home</a></li>
    <li><a href='/?page=about.md'>About</a></li>
    <li><a href='https://tom-ridge.blogspot.com/' target='_blank'>Blog</a></li>
    <li><a href='/?page=filesystems.md'>Filesystems</a></li>
    <li><a href='/?page=parsing.md'>Parsing</a></li>
    <li><a href='/?page=publications.md'>Publications</a></li>
    <li><a href='/?page=software.md'>Software</a></li>
  </ul>
</div>
"""


# header ---------------------------------------------------------------


# https://www.w3schools.com/howto/howto_js_topnav.asp
header_css="""
/* Add a black background color to the top navigation */
.topnav {
  background-color: #333;
  overflow: hidden;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Add a color to the active/current link */
.topnav a.active {
  background-color: #4CAF50;
  color: white;
}

/* https://coder-coder.com/display-divs-side-by-side/ */
.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 0px;
}
"""

header=f"""
<div style='text-align:right'>
  <h1>Tom Ridge</h1>       
  <p style='margin-top:0px;margin-bottom:20px'>
    Programmer, recovering academic</p>
  {social_bar()}
</div>
<br/>
{navbar}
<br/>
"""


title="Tom Ridge's homepage"

# md=""
# with open('index.md','r') as reader:
#     md=reader.read()
# 
# markdown_as_html=markdown.markdown(md)

# marked_script="""
#     <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
#     <script>
#     // https://www.sitepoint.com/get-url-parameters-with-javascript/
#     const queryString = window.location.search;
#     const urlParams = new URLSearchParams(queryString);
# 
#     // check if we need to redirect to old site
#     var old = urlParams.get('old');
#     oldsite="http://tomjridge.github.io/oldsite/"
#     if (old!==null) { window.location.replace(oldsite+old); }
# 
#     var page = urlParams.get('page');
#     if (page==null) { page="index.md"; }
#     console.log("page is "+page)
#     
#     var oreq = new XMLHttpRequest();
#     oreq.onload = function(e) {
#         document.getElementById('content').innerHTML =
#           marked.marked(oreq.response);
#     }
#     oreq.open("GET",page);
#     oreq.send();
#     </script>
# """

markdownit_script = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/markdown-it/12.2.0/markdown-it.min.js" integrity="sha512-cTQeM/op796Fp1ZUxfech8gSMLT/HvrXMkRGdGZGQnbwuq/obG0UtcL04eByVa99qJik7WlnlQOr5/Fw5B36aw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script>
// https://www.sitepoint.com/get-url-parameters-with-javascript/
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

// check if we need to redirect to old site
var old = urlParams.get('old');
oldsite="http://tomjridge.github.io/oldsite/"
if (old!==null) { window.location.replace(oldsite+old); }

var page = urlParams.get('page');
if (page==null) { page="index.md"; }
console.log("page is "+page)

var md = window.markdownit();
// we need to set options on md
md.set({ html:true, typographer:true });

var oreq = new XMLHttpRequest();
oreq.onload = function(e) {
    document.getElementById('content').innerHTML =
      md.render(oreq.response);
}
oreq.open("GET",page);
oreq.send();
</script>
"""

meta_no_cache="""
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Expires" content="0" />
"""

template= f"""
<!DOCTYPE html>
<html>

  <!-- header ---------------------------------------- -->

  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="robots" content="all,follow" />

    {meta_no_cache}

    <meta name="author" content="Tom Ridge" />
    <meta name=viewport content="width=device-width, initial-scale=1">
    
    {font_awesome_head}

    <title>{title}</title>

    <style>
      {base_css}
      {header_css}
      {navbar_css}
    </style>

  </head>

  <body>
    <div style='max-width:40em; margin:auto;'>
      {header}    

      <!-- main post ---------------------------------------- -->
      <div id='content' style='max-width:30em;margin:0px'>
        <!-- gets replaced with content via marked_script -->
      </div>

      {markdownit_script}

      <!-- bottom nav -->
      <div style='margin-top:10px'> {navbar} </div>
  </body>

</html>
"""


print(template)



# sticky notes ---------------------------------------------------------

# OLD 2021-03-24


# timeline -------------------------------------------------------------

# OLD 2021-03-24

# w3 cards -------------------------------------------------------------

# OLD 2021-03-24


unused_css="""
.title {
    font-size: 40px;
    padding: 1em 0;
}


.date {
  font-family: sans-serif;
  padding: 0.5em 0;
}

.categories {
  font-family: sans-serif;
  padding: 0.2em 0;
}


.note {
  width:12em;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-align:center;
  font-family: 'Pacifico', cursive;
  background: #ee5;
  margin:10px;
}
"""


# mathjax
mathjax_scripts="""
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
"""
