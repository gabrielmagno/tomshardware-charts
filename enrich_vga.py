#!/usr/bin/env python3

import sys
import json
import re

for line in sys.stdin:

    obj = json.loads(line)

    # Vendor 
    search_vendor = re.search("^(\S+)", obj["prod_name"])
    obj["vga_vendor"] = search_vendor.group(1)

    # Core 
    search_clock = re.search("(\d+)\s*M[Hh]z(\+)?\s*(?:\((\*emul)\))?((?:Crossfire)|(?:SLI))?", obj["prod_detail"])
    clock_mhz, overclock, emul, multi = search_clock.groups()

    obj["vga_clock_mhz"] =  int(clock_mhz)
    obj["vga_overclock"] =  int(bool(overclock)) 
    obj["vga_emul"] =  int(bool(emul))
    obj["vga_multi"] =  int(bool(multi))

    # Memory
    search_memory = re.search("(?:(\d+)x)?\s*(\d+)\s*GB", obj["prod_detail"])
    n_devices, mem_gb = search_memory.groups() 

    obj["vga_n_devices"] = int(n_devices) if n_devices else 1
    obj["vga_mem_gb"] = int(mem_gb)

    sys.stdout.write("{}\n".format(json.dumps(obj)))

