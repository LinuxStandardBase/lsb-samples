#
#	Copyright 1999, International Business Machines, Inc.
#	George Kraft IV (gk4@us.ibm.com)
#       Christopher Yeoh (cyeoh@linuxcare.com)
#
#	Red Hat Package Manager (RPM) file for lsb-release
#
# Note that in order to create a package which is LSB compliant
# the value of the _defaultdocdir macro should be /usr/share/doc
# and _mandir should be /usr/share/man
#

Summary: Linux Standard Base tools
Name: lsb-release
Version: 1.4
Release: 1
Copyright: GPL
Source: lsb-release-1.3.tgz
Group:  System/Tools
URL:  http://www.linuxbase.org/
Vendor: Linux Standard Base
Packager: Christopher Yeoh <cyeoh@linuxcare.com>
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-root
Prefix: %{_prefix}

%description
Linux Standard Base (LSB) tools.

%prep

%setup

%build
rm -rf $RPM_BUILD_ROOT
make

%install
make prefix=%buildroot mandir=%buildroot/%{_mandir} install 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc lsb-release.template
/bin/lsb_release
%{_mandir}/man1/lsb_release.1*

%changelog
* Mon Nov  6 2000 Christopher Yeoh <cyeoh@linuxcare.com>
- Repackage for version 1.4
- Add comments about creating an LSB compliant package.

* Thu Nov  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- add %defattr to fix build as non root.
- fix %file for non rh distribution.
- macros.

* Mon Oct 30 2000 Christopher Yeoh <cyeoh@linuxcare.com>
- Repackage so lsb_release goes in /bin

* Sat Oct 21 2000 Christopher Yeoh <cyeoh@linuxcare.com>
- Changes for 1.2 release of lsb_release

* Thu Sep 28 2000 Christopher Yeoh <cyeoh@linuxcare.com>
- Changes for 1.1 release of lsb_release

* Tue Sep 26 2000 Christopher Yeoh <cyeoh@linuxcare.com>
- Clean up script not to trample over currently installed package
- Changes to use new makefile bundled with lsb_release tarball
- Fixes bugs in post commands and adds post uninstall commands

