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

Note that your EchoNest API key must be set as an environment variable: `ECHO_NEST_API_KEY`
If you don't have a key, register at [developer.echonest.com](http://developer.echonest.com).

