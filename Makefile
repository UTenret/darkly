ENUMERATION_DIR := KaliLists
PASSWORDS_DIR := SecLists

setup:
	brew install gobuster
	pip install -r requirements.txt
	@if [ ! -d "$(ENUMERATION_DIR)" ]; then \
		git clone git@github.com:3ndG4me/$(ENUMERATION_DIR).git; \
	fi
	@if [ ! -d "$(PASSWORDS_DIR)" ]; then \
		git clone git@github.com:danielmiessler/$(PASSWORDS_DIR).git; \
	fi
	rm -rf $(ENUMERATION_DIR)/.git  $(PASSWORDS_DIR)/.git

clean:
	rm -rf $(ENUMERATION_DIR) $(PASSWORDS_DIR)

resetup:
	@$(MAKE) clean
	@$(MAKE) setup