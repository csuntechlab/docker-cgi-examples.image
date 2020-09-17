#! /bin/bash


# A simple CGI script the emits all fo the CGI variables


# Basic Request via the HTTP Protocol
#
# METHOD URI?QUERY PROTOCOL
# server: HOST
# <other request headers>
# <blank line>
# <optional body>

# Basic CGI Response

# Emit response headers
echo "X-function: Emiting a hereis document"
echo "Content-type: text/html"
echo ""

# Emit blank line
echo ""

# Emit body
cat <<EOF
<!-- Start of the Body -->
<html>
  <head>
     <title>Hello!</title>
  </head>
  <body>
    <h1>A Simple HTML Document</h1>
    "Hello!"
  </body>
</html>
<!-- End of the Body -->
EOF
