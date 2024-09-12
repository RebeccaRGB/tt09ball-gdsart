module the_ROMest (
	input wire [2:0] addr,
	output wire [7:0] data1,
	output wire [7:0] data2
);

	reg [7:0] mem1[7:0];
	initial begin
		mem1[0] = 8'h6F;
		mem1[1] = 8'h00;
		mem1[2] = 8'h39;
		mem1[3] = 8'h30;
		mem1[4] = 8'h31;
		mem1[5] = 8'h37;
		mem1[6] = 8'h3F;
		mem1[7] = 8'h00;
	end

	reg [7:0] mem2[3:0];
	initial begin
		mem2[0] = 8'h42;
		mem2[1] = 8'h41;
		mem2[2] = 8'h4B;
		mem2[3] = 8'h41;
	end

	assign data1 = mem1[addr[2:0]];
	assign data2 = mem2[addr[1:0]];

endmodule
