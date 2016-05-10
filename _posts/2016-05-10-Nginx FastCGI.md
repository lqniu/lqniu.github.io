---
layout: post
title: "Nginx&FastCGI"
date:   2016-05-09 15:49:53
categories: work
tags: Nginx Linux
---

{% highlight bash %}
wget http://download.lighttpd.net/spawn-fcgi/releases-1.6.x/spawn-fcgi-1.6.4.tar.gz
tar -xzvf spawn-fcgi-1.6.4.tar.gz
cd spawn-fcgi-1.6.4
ls
./configure
make
make install
{% endhighlight %}

{% highlight bash %}
yum install fcgi-devel -y
{% endhighlight %}

{% highlight bash %}
g++ main.cpp -o demo -lfcgi
spawn-fcgi -a 127.0.0.1 -p 8080 -f demo
nginx -s reloadls
{% endhighlight %}

{% highlight bash %}
location ~.*\.cgi$ {
  fastcgi_pass 127.0.0.1:8080;
  fastcgi_index index.cgi;
  include fastcgi.conf;
}
{% endhighlight %}

{% highlight cpp %}
#include "fcgi_stdio.h"
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
int main(void){
  int count = 0;
  while( FCGI_Accept() >= 0){    
    printf("Content-type:text/html\r\n");
    printf("\r\n");
    printf("<title>FastCGI Hello!</title>");
    printf("<h1>FastCGI Hello!</h1>");
    printf("Request number %d running on host <i>%s</i>\n",
      ++count,getenv("SERVER_NAME"));
    printf("Process Id: %d", getpid());
    char * method = getenv("REQUEST_METHOD");
    if (!strcmp(method, "POST")) {
      int ilen = atoi(getenv("CONTENT_LENGTH"));
      char *bufp =(char*) malloc(ilen);
      fread(bufp, ilen, 1, stdin);
      printf("The POST data is<p>%s\n", bufp);
      free(bufp);
    }
  }
  return 0;
}
{% endhighlight %}

ref:http://www.cnblogs.com/skynet/p/4173450.html
