%define upstream_name    SNMP-Info
%define upstream_version 2.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Object Oriented Perl5 Interface to Network devices and MIBs through SNMP
License:    BSD-like
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/SNMP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-NetSNMP >= 5.1.2
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT ChangeLog DeviceMatrix.txt README
%{perl_vendorlib}/SNMP
%{_mandir}/*/*
