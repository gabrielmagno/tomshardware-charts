#!/bin/bash

INFILE=$1

jq -r '[.chart_name, .bench_name, .bench_detail, .prod_id, .prod_group, .prod_name, .prod_detail, .score] | @csv' $INFILE

