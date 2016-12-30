# watts

[![Code Health](https://landscape.io/github/nschloe/watts/master/landscape.png)](https://landscape.io/github/nschloe/watts/master)
[![PyPi Version](https://img.shields.io/pypi/v/watts.svg)](https://pypi.python.org/pypi/watts)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/watts.svg?style=social&label=Star&maxAge=2592000)](https://github.com/nschloe/watts)

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
      - data:
          - date: 2015-01-01T00:00:00+00:00
            value: 0
          - date: 2016-03-01T00:00:00+00:00
            value: 100
```
you'll get
```
watts test.yml
```

![](https://nschloe.github.io/watts/example.png)

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
      - id: abc123
        data:
          - date: 2013-01-01T00:00:00+00:00
            value: 0.0
          - date: 2013-07-01T00:00:00+00:00
            value: 2.0
          - date: 2014-01-01T00:00:00+00:00
            value: 3.0
      - id: abc124
        data:
          - date: 2014-01-01T00:00:00+00:00
            value: 0.0
          - date: 2014-07-01T00:00:00+00:00
            value: 1.0
          - date: 2015-01-01T00:00:00+00:00
            value: 2.0

  # cold
  - style:
      color: '#1f77b4'
    meters:
      - id: def123
        data:
          - date: 2012-01-01T00:00:00+00:00
            value: 0.0
          - date: 2014-07-01T00:00:00+00:00
            value: 1.0
          - date: 2015-01-01T00:00:00+00:00
            value: 2.0
```

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    $ make publish
    ```


### License

watts is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
