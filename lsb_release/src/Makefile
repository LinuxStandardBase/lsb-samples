# 
# Makefile for lsb_release program
#

# Config
prefix=/opt/lsb

all: man

man: lsb_release.1.gz

lsb_release.1.gz: lsb_release
	@cp -p lsb_release lsb_release.orig
	@cat lsb_release.orig | sed -e "s/\[ -n \"\$ARG_V\" \] \&\& DisplayVersion/\[ -n \"\$ARG_V\" \] \&\& Version/" >./lsb_release
	@chmod a+x ./lsb_release
	@./help2man -N --include ./lsb_release.examples ./lsb_release >lsb_release.1
	@mv lsb_release.orig lsb_release
	@gzip -f lsb_release.1

install: all
	install -D -m 644 lsb_release.1.gz ${prefix}/man/man1/lsb_release.1.gz
	install -D -m 755 lsb_release ${prefix}/bin/lsb_release
