%define srcname kafka-python

Name:           python-kafka
Version:        2.0.2
Release:        0.1%{?dist}
Summary:        Pure Python client for Apache Kafka

Group:          Development/Libraries
License:        Apache 2.0
URL:            https://github.com/dpkp/kafka-python
Source0:        https://pypi.python.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

## For test suite
#BuildRequires:  python3dist(tox)
#BuildRequires:  python3dist(mock)

%global _description\
Python client for the Apache Kafka distributed stream processing system.\
kafka-python is designed to function much like the official java client,\
with a sprinkling of pythonic interfaces (e.g., consumer iterators).\
\
kafka-python is best used with newer brokers (0.9+), but is\
backwards-compatible with older versions (to 0.8.0).\
Some features will only be enabled on newer brokers.

%description %_description

%package -n python3-kafka

Summary:        %summary
Requires:       python3dist(setuptools)
%{?python_provide:%python_provide python3-kafka}

%description -n python3-kafka  %_description


%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

#%check
# Disabled because the tox configuration file is not included
# in official tarball, even though the tests are.
#PYTHONPATH=$(pwd) tox -e py27

%files -n python3-kafka
%defattr(-,root,root,-)
%doc PKG-INFO README.rst
%license LICENSE
%{python3_sitelib}/kafka
%{python3_sitelib}/kafka_python-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 06 2021 François Poirotte <francois.poirotte@csnovidys.com> - 2.0.2-0.1
- Initial package for rawhide and EL8.
