#!/bin/bash

python crawler/crawl_chart.py "http://www.tomshardware.com/charts/2015-vga-charts/benchmarks,186.html" > data/vga_2015.jsonl

python crawler/enrich_vga.py < "data/vga_2015.jsonl" > "data/vga_2015-enriched.jsonl"

echo "chart_name,bench_name,bench_detail,prod_id,prod_name,prod_detail,vga_vendor,vga_clock_mhz,vga_mem_gb,vga_n_gpus,vga_overclock,vga_multi,vga_emul,score" >"data/vga_2015-enriched.csv"

jq -r '[.chart_name, .bench_name, .bench_detail, .prod_id, .prod_name, .prod_detail, .vga_vendor, .vga_clock_mhz, .vga_mem_gb, .vga_n_gpus, .vga_overclock, .vga_multi, .vga_emul, .score] | @csv' "data/vga_2015-enriched.jsonl" >> "data/vga_2015-enriched.csv"

#python crawler/crawl_benchmark.py "http://www.tomshardware.com/charts/cpu-charts-2015/benchmarks,187.html" > data/cpu_2015.jsonl

