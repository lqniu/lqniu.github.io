# -*- coding: utf-8 -*-  
from pyh import *
page=PyH("目录")
pyge.addMEAT()
page.addJS("http://cdn.bootcss.com/jquery/1.11.2/jquery.min.js")
page.addJS("js/bootstrap.min.js")
page<<h1('炼神领域',cl='center')
page.printOut("test.html")
