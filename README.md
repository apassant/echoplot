echoplot
========

Plot song data using the EchoNest API

Usage
-----

    pip install echoplot

This will install the python module and the echoplot helper script

    echoplot 'The Clash' 'London Calling'

or

    #!/usr/bin/env python

    from echoplot import EchoPlot

    EchoPlot('The Clash', 'London Calling').plot()
