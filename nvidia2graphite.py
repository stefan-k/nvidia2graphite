#!/usr/bin/env python3
"""Send metrics from NVIDIA GPUs to Graphite

Uses nvidia-smi to collect metrics about NVIDIA GPUs and sends the data to
graphite. The configuration is done in nvidia2graphite.conf which is located
in /etc/ after installation. The server as well as the sent metrics are defined
there.

Installation command (as superuser):
    $ python3 setup.py install

Note: Uses Python3 but may work with python2 too (not tested).

Requirements: graphitesend

License: MIT

Author: Stefan Kroboth <stefan.kroboth@uniklinik-freiburg.de>
"""

from __future__ import print_function
import subprocess
import configparser
from xml.etree import ElementTree
import re
import time
import graphitesend

# pylint: disable=invalid-name

if __name__ == '__main__':
    # Read in the config file
    conf = configparser.ConfigParser()
    conf.read('/etc/nvidia2graphite.conf')

    # Extract metrics
    metrics = []
    for key in conf['Metrics']:
        metrics.append(conf['Metrics'][key])

    # Extract graphite server information
    dryrun = False
    graphite_server = conf['Graphite']['host']
    graphite_port = int(conf['Graphite']['port'])
    wait_time = float(conf['Graphite']['interval'])

    while 1:
        data = subprocess.check_output(['nvidia-smi', '-q', '-x'])
        root = ElementTree.fromstring(data)

        # Loop over GPUs
        gpu_id = 1
        for gpu in root:
            # ignore non-gpu tags
            if gpu.tag != 'gpu':
                continue

            # parse XML data and compile dictionary
            metric_dict = dict()
            for metric in metrics:
                curr_level = gpu
                for level in metric.split('.'):
                    curr_level = curr_level.find(level)
                data = re.sub(r"\D", "", curr_level.text)
                if data is not None and data != '':
                    metric_dict[metric] = data

            # setup graphite and send dictionary
            g = graphitesend.init(group='gpu' + str(gpu_id),
                                  graphite_server=graphite_server,
                                  graphite_port=graphite_port,
                                  dryrun=dryrun)
            g.send_dict(metric_dict)

            gpu_id += 1

        time.sleep(wait_time)
