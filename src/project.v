/*
 * Copyright (c) 2024 Rebecca G. Bettencourt
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

`ifdef USE_LOGO
`include "logo.vh"
`endif

module tt_um_rebeccargb_tt09ball_gdsart (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  reg [2:0] counter;

  always @(posedge clk) begin
    if (~rst_n) begin
      counter <= 0;
    end else begin
      counter <= counter + 1;
    end
  end

  // All output pins must be assigned. If not used, assign to 0.
  the_ROMest rom((ui_in[3] ? ui_in[2:0] : counter), uo_out, uio_out);
  assign uio_oe = 8'hFF;

  // List all unused inputs to prevent warnings
  wire _unused_ok = &{ui_in[7:4], uio_in, ena};

// Add logo design
`ifndef GL_TEST
`ifdef USE_LOGO
  (* keep *)
  `LOGO_NAME `LOGO_INSTANCE();
`endif
`endif

endmodule
