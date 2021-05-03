ifeq ($(PACKAGE_SET),dom0)
  RPM_SPEC_FILES = qubes-network-server.spec
else ifeq ($(PACKAGE_SET),vm)
  RPM_SPEC_FILES = qubes-network-server-vm.spec
endif
