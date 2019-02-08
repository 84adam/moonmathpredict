# moonmathpredict

See: https://www.moonmath.win/

Compound Interest Function from: https://www.geeksforgeeks.org/python-program-for-compound-interest/

Uses a static (manually-entered) price currently.

Compound Daily Periodic Rate (CDPR) is based on a slightly-modified, weighted average from moonmath.win, years 2010-2017:
rates for each year = `[0.1594, 0.1814, 0.1589, 0.0795, 0.2489, 0.2496, 0.3159, 0.3391]`

Then I assume two more years of middling CDPR like 2014 (append 0.0795 twice to the list), then take a weighted average: 2019x1, 2018x1, 2017x1, and for each previous year weight it one higher, so: 2016x2, 2015x3, etc. Finally, sum and average (/38 items in the list) to get my estimate.

**My estimated CDPR for bitcoin is: 0.2406 %.**

Moonmath.win projects a CDPR of 0.3 %.

See: https://www.moonmath.win/faq.html
