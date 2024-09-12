# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x6F
    assert dut.uio_out.value == 0x42

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x00
    assert dut.uio_out.value == 0x41

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x39
    assert dut.uio_out.value == 0x4B

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x30
    assert dut.uio_out.value == 0x41

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x31
    assert dut.uio_out.value == 0x42

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x37
    assert dut.uio_out.value == 0x41

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x3F
    assert dut.uio_out.value == 0x4B

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x00
    assert dut.uio_out.value == 0x41

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x6F
    assert dut.uio_out.value == 0x42

    dut.ui_in.value = 8
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x6F
    assert dut.uio_out.value == 0x42

    dut.ui_in.value = 9
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x00
    assert dut.uio_out.value == 0x41

    dut.ui_in.value = 10
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x39
    assert dut.uio_out.value == 0x4B

    dut.ui_in.value = 11
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x30
    assert dut.uio_out.value == 0x41

    dut.ui_in.value = 12
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x31
    assert dut.uio_out.value == 0x42

    dut.ui_in.value = 13
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x37
    assert dut.uio_out.value == 0x41

    dut.ui_in.value = 14
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x3F
    assert dut.uio_out.value == 0x4B

    dut.ui_in.value = 15
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x00
    assert dut.uio_out.value == 0x41

    dut.ui_in.value = 8
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x6F
    assert dut.uio_out.value == 0x42
