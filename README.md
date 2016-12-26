# watts

This little script takes a number of energy measurements (e.g., from your
electricity meter or old power bills) and displays the wattage over time.

For example, with the data file
```
- date: 2016-01-01 00:00
  value: 10
- date: 2016-02-01 00:00
  value: 12
- date: 2016-04-01 00:00
  value: 20
- date: 2016-07-01 00:00
  value: 35
- date: 2016-10-01 00:00
  value: 40
```
you'll get
```
./show_data test.yml
```

![](https://nschloe.github.io/watts/example.png)

The `value`s are assumed to be given in kWh.

### License

watts is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
