%define srcname urllib_kerberos

Name:           python-urllib-kerberos
Version:        0.2.0
Release:        1%{?dist}
Summary:        Kerberos over HTTP Negotiate/SPNEGO support for urllib2

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}/
Source0:        https://pypi.python.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
urllib2 with Kerberos authentication.

%description %_description

%package -n python3-urllib-kerberos
Summary:        %summary
Requires:       python3dist(kerberos)
%{?python_provide:%python_provide python3-urllib-kerberos}

%description -n python3-urllib-kerberos %_description

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%check
# The tests are disabled because they require internet access.

%files -n python3-urllib-kerberos
%defattr(-,root,root,-)
%{python3_sitelib}/%{srcname}*

%changelog
* Fri Feb 12 2021 Francois Poirotte <francois.poirotte@csnovidys.com> - 0.2.0-1
- Initial package.
