#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import psutil ;
mem = psutil.virtual_memory();
mem.total,mem.used;
print (mem.total,mem.used);