%define upstream_name    SNMP-Info
%define upstream_version 3.11
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Object Oriented Perl5 Interface to Network devices and MIBs through SNMP
License:	BSD-like
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SNMP/SNMP-Info-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(SNMP)
BuildArch:	noarch

%description
SNMP::Info gives an object oriented interface to information obtained
through SNMP.

This module lives at http://snmp-info.sourceforge.net Check for newest
version and documentation.

This module is geared towards network devices. Subclasses exist for a
number of network devices and common MIBs.

The idea behind this module is to give a common interface to data from
network devices, leaving the device-specific hacks behind the scenes in
subclasses.

In the SYNOPSIS example we fetch the name of all the ports on the device
and the duplex setting for that port with two methods -- interfaces()
and i_duplex().

The information may be coming from any number of MIB files and is very
vendor specific. SNMP::Info provides you a common method for all
supported devices.
                                
Adding support for your own device is easy, and takes little much SNMP
knowledge.
                                    
The module is not limited to network devices. Any MIB or device can be
given an objected oriented front-end by making a module that consists of
a couple hashes. See EXTENDING SNMP::INFO.
                                    

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc COPYRIGHT ChangeLog DeviceMatrix.txt README
%{perl_vendorlib}/SNMP
%{_mandir}/*/*


%changelog
* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.50.0-1mdv2011.0
+ Revision: 686994
- update to new version 2.05

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.40.0-1
+ Revision: 654375
- update to new version 2.04

  + Olivier Thauvin <nanardon@mandriva.org>
    - rebuild for new perl

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.10.0-1mdv2010.0
+ Revision: 404388
- rebuild using %%perl_convert_version

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2010.0
+ Revision: 387031
- update to new version 2.01

* Mon Aug 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.00-1mdv2009.0
+ Revision: 262839
- 2.00

* Wed Jul 23 2008 Oden Eriksson <oeriksson@mandriva.com> 1.09-0.beta.1mdv2009.0
+ Revision: 242192
- 1.09

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Oden Eriksson <oeriksson@mandriva.com> 1.07-0.beta.1mdv2008.1
+ Revision: 113304
- 1.07 (beta)

* Fri Apr 27 2007 Oden Eriksson <oeriksson@mandriva.com> 1.04-2mdv2008.0
+ Revision: 18588
- rebuild


* Wed Nov 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.04-1mdv2007.0
+ Revision: 88286
- Import perl-SNMP-Info

* Wed Nov 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.04-2mdv2007.1
- rebuild

* Wed Jul 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2007.0
- new version
- rpmbuildupdate aware
- spec cleanup

* Tue Jan 31 2006 Oden Eriksson <oeriksson@mandriva.com> 1.03-0.beta.1mdk
- 1.03beta

* Tue Jan 31 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.20060124.1mdk
- use a recent snap (20060124)

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.0-1mdk
- New release 0.9.0
- rpmbuildupdate aware
- better url
- fix directory ownership
- fix summary

* Fri Aug 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8-2mdk
- BuildRequires: perl-NetSNMP >= 5.1.2 and not perl-Net-SNMP >= 5.1.2

* Fri Aug 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8-1mdk
- initial mandrake package






