#!/usr/bin/env python3

import sys
import urllib.request
import re
import json

# Regular expressions

RE_CHART = re.compile("<h3>(?P<chart_name>[^<]+)</h3>", re.DOTALL)

RE_BENCHMARKS = re.compile("<a href=\"(?P<bench_url>[^\"]+)\" title=\"[^\"]+\">(?P<bench_name>[^<]+)</a><br />\s*<span>[^<]+</span>\s*<span>\((?P<bench_detail>[^<]+)\)</span>", re.DOTALL)

RE_PRODUCTS = re.compile("<div class=\"clLeft\">\s*<input type=\"checkbox\" name=\"prod\[(?P<prod_id>\d+)\]\" class=\"[^\"]+\" id=\"(?P<prod_group>[^\"]+)\" />\s*<label for=\"[^\"]+\">(?P<prod_name>[^<]+)</label>\s*<br />\s*<ul style=\"[^\"]+\">\s*<li><span>(?P<prod_detail>[^<]+)</span></li>\s*</ul>\s*</div>\s*<div class=\"clRight clearfix\">\s*<span style=\"[^\"]+\" class=\"scoreBlock\">\s*<span style=\"[^\"]+\">\s*(?P<score>[\d\.]+)\s*</span>", re.DOTALL)


#url_chart = "http://www.tomshardware.com/charts/2015-vga-charts/benchmarks,186.html"
url_chart = sys.argv[1]

# Collect chart info
html = urllib.request.urlopen(url_chart).read().decode("UTF-8")
chart = RE_CHART.search(html).groupdict()

# Collect list of benchmarks
benchmarks = [ m.groupdict() for m in RE_BENCHMARKS.finditer(html) ]
for benchmark in benchmarks:

    # Collect scores of products in the benchmark
    html = urllib.request.urlopen(benchmark["bench_url"]).read().decode("UTF-8")
    products = [ m.groupdict() for m in RE_PRODUCTS.finditer(html) ]

    for product in products:

        row = {
            "chart_name"   : chart["chart_name"],

            "bench_name"   : benchmark["bench_name"],
            "bench_detail" : benchmark["bench_detail"],
            
            "prod_id"      : product["prod_id"],
            "prod_group"   : product["prod_group"],
            "prod_name"    : product["prod_name"],
            "prod_detail"  : product["prod_detail"],

            "score"        : float(product["score"])
        }

        sys.stdout.write("{}\n".format(json.dumps(row)))

