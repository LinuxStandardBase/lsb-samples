#
#	Copyright 1999, International Business Machines, Inc.
#	George Kraft IV (gk4@us.ibm.com)
#
#	Red Hat Package Manager (RPM) file for LSB
#
Summary: Linux Standard Base tools
Name: lsb_release
Version: 1.1
Release: 1
Prefix: /opt
Copyright: GPL
Source: lsb-release-1.0.tgz
Group:  System/Tools
URL:  http://www.linuxbase.org/
Vendor: Linux Standard Base
Packager: George Kraft IV <gk4@us.ibm.com>
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-root

%description
Linux Standard Base (LSB) tools.

%prep

%setup

%build
rm -rf $RPM_BUILD_ROOT
make

%install
make prefix=${RPM_BUILD_ROOT}%{prefix}/lsb install 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{prefix}/lsb/bin/lsb_release
%{prefix}/lsb/man/man1/lsb_release.1.gz

%post
P=$RPM_INSTALL_PREFIX
mkdir -p $P/bin/ > /dev/null 2>&1
ln -fs $P/lsb/bin/lsb_release $P/bin/
mkdir -p $P/man/man1/ > /dev/null 2>&1
ln -fs $P/lsb/man/man1/lsb_release.1.gz $P/man/man1/

%postun
rm -f $RPM_INSTALL_PREFIX/bin/lsb_release
rm -f $RPM_INSTALL_PREFIX/man/man1/lsb_release/lsb_release.1.gz

%changelog
* Thu Sep 28 2000 Christopher Yeoh <cyeoh@linuxcare.com>
- Changes for 1.1 release of lsb_release

* Tue Sep 26 2000 Christopher Yeoh <cyeoh@linuxcare.com>
- Clean up script not to trample over currently installed package
- Changes to use new makefile bundled with lsb_release tarball
- Fixes bugs in post commands and adds post uninstall commands
