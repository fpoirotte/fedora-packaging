%define upstream_name Math-RPN

Name:           perl-%{upstream_name}
Version:        1.11
Release:        0.1%{?dist}
Summary:        Perl extension for Reverse Polish Math Expression Evaluation

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{upstream_name}
Source0:        https://cpan.metacpan.org/modules/by-module/Math/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Module::Install)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The rpn function will take a scalar or list of scalars which contain an RPN
expression as a set of comma-delimited values and operators, and return the
result or stack, depending on context.

%prep
%setup -q -n %{upstream_name}-%{version}

# remove errant execute bits
find . -type f -exec chmod -x {} ';'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*


%check
make test


%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Fri Jan 08 2021 Francois Poirotte <francois.poirotte@c-s.fr> - 1.11-0.1
- Update to 1.11 and build for EL8
