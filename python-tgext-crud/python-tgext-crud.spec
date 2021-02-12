%global pypi_name tgext.crud

Name:           python-tgext-crud
Version:        0.9.0
Release:        1%{?dist}
Summary:        CRUD Controller Extension for TurboGears2

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%global _description\
Automatically creates CRUD and REST-APIS based on a SQLAlchemy or Ming model.

%description %_description

%package -n python3-tgext-crud
Summary:        %summary
Requires:       python3-sprox
Requires:       python3-TurboGears2
%{?python_provide:%python_provide python3-tgext-crud}

%description -n python3-tgext-crud %_description

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-tgext-crud
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py*
%{python3_sitelib}/tgext/crud/
%exclude %{python3_sitelib}/tests

%changelog
* Fri Feb 12 2021 Francois Poirotte <francois.poirotte@csnovidys.com> - 0.8.2-1
- Repackage for Rawhide.
