# meterplot

[![Build Status](https://travis-ci.org/nschloe/meterplot.svg?branch=master)](https://travis-ci.org/nschloe/meterplot)
[![codecov](https://codecov.io/gh/nschloe/meterplot/branch/master/graph/badge.svg)](https://codecov.io/gh/nschloe/meterplot)
[![PyPi Version](https://img.shields.io/pypi/v/meterplot.svg)](https://pypi.python.org/pypi/meterplot)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/meterplot.svg?style=social&label=Stars)](https://github.com/nschloe/meterplot)

This little script takes a number of energy measurements (e.g., from your
electricity meter or old power bills) and displays the consumption over time.
Works for electricity and water readings.

For example, with the data file
```yaml
# electricity data
---
unit: kWh
groups:
  - style:
      color: '#2ca02c'
    meters:
      - data:
          - date: 2016-01-01T00:00:00+00:00
            value: 1000
          - date: 2016-02-01T00:00:00+00:00
            value: 1200
          - date: 2016-04-01T00:00:00+00:00
            value: 2000
          - date: 2016-07-01T00:00:00+00:00
            value: 3500
          - date: 2016-10-01T00:00:00+00:00
            value: 4000
```
you'll get
```
meterplot electricity.yml
```

![](https://nschloe.github.io/meterplot/electricity.png)

Input of water data is equally easy (here for warm and cold water, with a meter
change)
```yaml
# Water data
---
unit: m^3

groups:
  # warm
  - style:
      color: '#d62728'
    meters:
      - data:
          - date: 2013-01-01T00:00:00+00:00
            value: 0.0
          - date: 2013-07-01T00:00:00+00:00
            value: 16.6
          - date: 2014-01-01T00:00:00+00:00
            value: 30.0
      - data:
          - date: 2014-01-01T00:00:00+00:00
            value: 0.0
          - date: 2014-07-01T00:00:00+00:00
            value: 15.2
          - date: 2015-01-01T00:00:00+00:00
            value: 25.1

  # cold
  - style:
      color: '#1f77b4'
    meters:
      - data:
          - date: 2013-01-01T00:00:00+00:00
            value: 0.0
          - date: 2013-04-01T00:00:00+00:00
            value: 4.0
          - date: 2014-07-01T00:00:00+00:00
            value: 23.0
          - date: 2015-01-01T00:00:00+00:00
            value: 35.1
```
```
meterplot electricity.yml
```

![](https://nschloe.github.io/meterplot/water.png)

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    $ make publish
    ```


### License

meterplot is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
