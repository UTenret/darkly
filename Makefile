ENUMERATION_DIR := KaliLists

setup:
	brew install gobuster hydra
	@if [ ! -d "$(ENUMERATION_DIR)" ]; then \
		git clone git@github.com:3ndG4me/$(ENUMERATION_DIR).git; \
	fi
	pip install -r requirements.txt

clean:
	rm -rf $(ENUMERATION_DIR)

resetup:
	@$(MAKE) clean
	@$(MAKE) setup