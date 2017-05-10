# nvidia2graphite

## Introduction

*nvidia2graphite* sends metrics from NVIDIA GPUs to Graphite.  
It uses nvidia-smi to collect metrics about NVIDIA GPUs and sends the data to
graphite. 

## Requirements

* [graphitesend](https://github.com/daniellawrence/graphitesend)
* Python3 (should work with Python2 too but may require small modifications)

## Installation

As superuser run:

```
python3 setup.py install
```

Enablethe service:

```
systemctl enable nvidia2graphite
```

Start the service:

```
systemctl start nvidia2graphite
```

Every change of the configuration (see next section) requires a restart of the servive.

## Configuration

The configuration is done in nvidia2graphite.conf which is located
in `/etc/` after installation. The graphite server as well as the extracted metrics are defined there.

## LICENSE

MIT License, see [LICENSE](LICENSE)
