#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 Peder Toftegaard Olsen
#
# SPDX-License-Identifier: MIT

import sys
try:
    from pyModbusTCP.client import ModbusClient
except ImportError:
    print("This example requires pyModbusTCP.")
    print("To install: python3 -m pip install pyModbusTCP")
    sys.exit(1)

RD_HOST = "rd6006-12345678.local"

c = ModbusClient(host=RD_HOST, port=502, unit_id=1, auto_open=True, timeout=2)
regs = c.read_holding_registers(0)

if regs:
    print(regs)
else:
    print("read error")