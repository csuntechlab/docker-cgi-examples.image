#! /bin/bash


# Basic Request via the HTTP Protocol
#
# METHOD URI?QUERY PROTOCOL
# server: HOST
# <other request headers>
# <blank line>
# <optional body>

# Basic CGI Response

# Emit response headers
echo "X-function: Emiting a document via cat"
echo "Content-type: text/plain"

# Emit blank line
echo ""

if [ -n "${QUERY_STRING}" ] ; then
    FILE_NAME="${QUERY_STRING}"
else
    FILE_NAME="cat.cgi"
fi

# Emit the contents of the file
cat ${FILE_NAME}



