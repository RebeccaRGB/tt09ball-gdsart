export PDK_ROOT = $(wildcard $(HOME)/.volare/volare/sky130/versions/*)
export CAD_ROOT = $(realpath $(PWD)/../../magic/release/lib)

MAGIC = $(realpath $(CAD_ROOT)/../bin/magic)
MAGIC_ARGS = -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc -noconsole

tt09ball4_logo.lef: tt09ball4_logo.gds
	(echo "gds read tt09ball4_logo.gds"; echo "load tt09ball4_logo"; echo "lef write tt09ball4_logo.lef"; echo "quit -noprompt") | $(MAGIC) $(MAGIC_ARGS) -dnull

tt09ball4_logo.gds: make_gds.py tt09ball4a.png
	python make_gds.py -i tt09ball4a.png -c tt09ball4_logo -o tt09ball4_logo.gds

run_magic:
	$(MAGIC) $(MAGIC_ARGS)

.PHONY: run_magic
