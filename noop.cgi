#! /bin/bash

# A simple CGI script that does nothing.
# Well, except adding a HTTP return header field.


# Emit response headers
echo "X-function: Echoing Request"
echo "Content-type: text/plain"

# Emit blank line
echo ""

# Emit body


:   # The noop command

exit 0