# 
# Makefile for lsb_release program
#

# Config
prefix=/opt/lsb

all: man

man: lsb_release.1.gz

lsb_release.1.gz: lsb_release
	@./help2man -N --include ./lsb_release.examples --alt_version_key=program_version ./lsb_release >lsb_release.1
	@gzip -f lsb_release.1

install: all
	install -D -m 644 lsb_release.1.gz ${prefix}/man/man1/lsb_release.1.gz
	install -D -m 755 lsb_release ${prefix}/bin/lsb_release
