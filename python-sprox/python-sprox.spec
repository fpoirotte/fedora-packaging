%global srcname sprox

Name:           python-%{srcname}
Version:        0.11.2
Release:        1%{?dist}
Summary:        A package for creation of web widgets directly from a database schema

Group:          Development/Languages
License:        MIT
URL:            https://github.com/TurboGears/%{srcname}/

# using github tarball instead, because it contains tests
Source0:        https://github.com/TurboGears/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch0:         python-sprox-py39.patch
Patch1:         python-sprox-doctests.patch
Patch2:         python-sprox-testbase.patch

BuildArch:      noarch

# For building
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-formencode >= 1.3.0

# For testing
BuildRequires:  python3-genshi
BuildRequires:  python3-mako
# Ming is not part of Fedora yet
#BuildRequires:  python3-ming
BuildRequires:  python3-nose
BuildRequires:  python3-sieve
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-tw2-forms

%global _description\
Sprox is a widget generation library that has a slightly different take on the\
problem of creating custom web content directly from a database schema. Sprox\
provides an easy way to create forms for web content which are: automatically\
generated, easy to customize, and validated. Sprox also has powerful tools to\
help you display your content the way you want to with table and record\
viewers. Sprox provides a way to fill your widgets, whether they are forms or\
other content with customizable data.

%description %_description

%package -n python3-%{srcname}
Summary:        %summary
Requires:       python3-formencode >= 1.3.0
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1 -b .py39
%patch1 -p1 -b .doctests
%patch2 -p1 -b .testbase

%build
%py3_build

%install
%py3_install
rm -fr %{buildroot}%{python3_sitelib}/tests

%check
PYTHONPATH=$(pwd) nosetests-%{python3_version} -v

%files -n python3-%{srcname}
%license license.txt
%doc CHANGELOG.txt
%{python3_sitelib}/%{srcname}*

%changelog
* Fri Feb 12 2021 Francois Poirotte <francois.poirotte@csnovidys.com> - 0.11.2-1
- Initial package for rawhide and EL8.
