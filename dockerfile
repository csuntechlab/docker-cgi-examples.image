FROM ubuntu

RUN apt-get clean && apt-get autoremove

LABEL project=docker-cgi
LABEL organization="AdvancingTechnology Laboratory (@dvancingTech) at CSUN"
LABEL image="Example Image for CGI programs"
LABEL version="0.1"
LABEL description="The image contains a suite of simple CGI programs that can be executed within a container on a webserver."
LABEL maintainer="Steven.Fitzgerald@csun.edu"

RUN mkdir /docker-cgi
ENV PATH="/docker-cgi:$PATH"

COPY noop.cgi		/docker-cgi/
COPY echo-request.cgi	/docker-cgi/
COPY emit-env.cgi	/docker-cgi/
COPY here.cgi		/docker-cgi/
COPY cat.cgi		/docker-cgi/

