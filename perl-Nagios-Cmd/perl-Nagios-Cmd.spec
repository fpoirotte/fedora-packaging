%define upstream_name Nagios-Cmd

Name: perl-%{upstream_name}
Version: 0.05
Release: 0.1%{?dist}

Summary:   Read a fifo or regular file like Nagios does
License:   GPL+ or Artistic
URL:       https://metacpan.org/release/%{upstream_name}
Source0:   https://cpan.metacpan.org/modules/by-module/Nagios/%{upstream_name}-%{version}.tar.gz
Buildarch: noarch

BuildRequires: perl-interpreter
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Install)

%description
A module for reading a fifo or regular file similar to the way Nagios does.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Build.PL

%install
rm -rf %{buildroot}
./Build install --destdir %{buildroot} installdirs=vendor
find %{buildroot} -name ".packlist" -exec rm -f '{}' \;

%check
# Upstream has no tests
#./Build test

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Nagios
%{_mandir}/*/*

%changelog
* Fri Jan 08 2021 Francois Poirotte <francois.poirotte@c-s.fr> - 0.05-0.1
- Initial package for rawhide/EL8
