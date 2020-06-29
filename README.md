# meterplot

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/meterplot/ci?style=flat-square)](https://github.com/nschloe/meterplot/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/meterplot.svg?style=flat-square)](https://codecov.io/gh/nschloe/meterplot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/meterplot.svg?style=flat-square)](https://pypi.org/project/meterplot)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/meterplot.svg?style=flat-square)](https://pypi.org/pypi/meterplot/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/meterplot.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/meterplot)
[![PyPi downloads](https://img.shields.io/pypi/dm/meterplot.svg?style=flat-square)](https://pypistats.org/packages/meterplot)

This little script takes a number of energy measurements (e.g., from your electricity
meter or old power bills) and displays the consumption over time.  Works for electricity
and water readings.

For example, with the data file
```yaml
# electricity data
---
unit: kWh
data:
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

Input of water data is equally easy (here for warm and cold water, with a meter change)
```yaml
# Water data
---
unit: m^3

- data:
    - date: 2013-01-01T00:00:00+00:00
      value: [0.0, 0.0]
    - date: 2013-07-01T00:00:00+00:00
      value: [16.6, 4.0]
    - date: 2014-01-01T00:00:00+00:00
      value: [30.0, 23.0]
    - date: 2014-01-01T00:00:00+00:00
      value: [0.0, 35.1]
    - date: 2014-07-01T00:00:00+00:00
      value: 15.2
    - date: 2015-01-01T00:00:00+00:00
      value: 25.1
```
```
meterplot water.yml
```

![](https://nschloe.github.io/meterplot/water.png)

### Installation

meterplot is [available from the Python Package Index](https://pypi.org/project/meterplot/), so with
```
pip install -U meterplot
```
you can install/upgrade.

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    $ make publish
    ```


### License

meterplot is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
