========
EchoPlot
========

Plot loudness of a song using the EchoNest API.

The EchoNest API key needs to be setup as an environment variable ECHO_NEST_API_KEY.

    #!/usr/bin/env python

    from echoplot import EchoPlot
    
    EchoPlot('The Clash', 'London Calling').plot()

Optional arguments ``start`` and ``end`` to start/end the song analysis at a certain time.

Note that your EchoNest API key must be set as an environment variable: ``ECHO_NEST_API_KEY``
If you don't have a key, register at <http://developer.echonest.com>.

Contact, infos, related hacks: <http://apassant.net> and <http://mdg.io>
