#
#	Copyright 1999, International Business Machines, Inc.
#	George Kraft IV (gk4@us.ibm.com)
#
#	Red Hat Package Manager (RPM) file for LSB
#
Summary: Linux Standard Base tools
Name: lsb_release
Version: 1.0
Release: 1 
Prefix: /opt
Copyright: GPL
Source: lsb_release-1.0.tgz
Group:  System/Tools
URL:  http://www.linuxbase.org/
Vendor: Linux Standard Base
Packager: George Kraft IV <gk4@us.ibm.com>

%description
Linux Standard Base (LSB) tools.

%prep
echo No speacial preparations are to be made.

%setup

%build
if [ ! -f "./lsb_release.ori" ]; then 
	# do a backup of lsb_release
	cp -p lsb_release lsb_release.ori
fi
mv -f lsb_release  lsb_release.tmp # lsb_release need to be parsed for
                                   # the help2man perl script
cat lsb_release.tmp | sed -e "s/\[ -n \"\$ARG_V\" \] \&\& DisplayVersion/\[ -n \"\$ARG_V\" \] \&\& Version/" >./lsb_release

chmod a+x ./lsb_release

rm -f lsb_release.1 lsb_release.1.bz2 # remove old man pages

# build man page
./help2man -N --include ./lsb_release.examples ./lsb_release >lsb_release.1

bzip2 lsb_release.1 # do the needed compression

# restore former lsb_release script
cat lsb_release | sed -e "s/\[ -n \"\$ARG_V\" \] \&\& Version/\[ -n \"\$ARG_V\" \] \&\& DisplayVersion/" >./lsb_release.tmp
mv -f lsb_release.tmp  lsb_release
chmod a+x ./lsb_release

cp lsb_release.1.bz2 /usr/man/man1/ # install place
cp lsb_release.1.bz2 /opt/lsb/man/man1/ # install place
ln -fs /opt/lsb/man/man1/lsb_release.1.bz2 /opt/man/man1 # install place

man -w lsb_release # view the result

%install
echo We assume a previous imake install on this system has occurred.

%files
/opt/lsb/bin/lsb_release
/opt/lsb/man/man1/lsb_release.1.bz2

%post
P=$RPM_INSTALL_PREFIX
mkdir $P/bin/ > /dev/null 2>&1
ln -fs $P/lsb/bin/lsb_release $P/bin/
mkdir $P/man/man1/ > /dev/null 2>&1
ln -fs $P/lsb/man/man1/lsb_release.1.bz2 $P/man/man1/

#EOF
