%global upstream_name txamqp

Name:           python-%{upstream_name}
Version:        0.8.2
Release:        1%{?dist}
Summary:        A Python library for communicating with AMQP peers and brokers using Twisted

License:        ASL 2.0
URL:            https://github.com/txamqp/txamqp
Source0:        https://files.pythonhosted.org/packages/source/t/txAMQP/txAMQP-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
txAMQP is a Python library for communicating with AMQP peers and brokers using\
Twisted.\
\
This project contains all the necessary code to connect, send and receive\
messages to/from an AMQP-compliant peer or broker (Qpid, OpenAMQ, RabbitMQ)\
using Twisted.

%description %_description

%package -n python3-%{upstream_name}
Summary:        Python 3 library for communicating with AMQP peers and brokers using Twisted
Requires:       python3-twisted
%{?python_provide:%python_provide python3-%{upstream_name}}

%description -n python3-%{upstream_name} %_description

%package -n python3-%{upstream_name}-thrift
Summary:        Contributed Thrift libraries for Twisted (Python 3)
Requires:       python3-%{upstream_name} = %{version}-%{release}
Requires:       python3-thrift
%{?python_provide:%python_provide python3-%{upstream_name}-thrift}

%description -n python3-%{upstream_name}-thrift
txAMQP also includes support for using Thrift RPC over AMQP in Twisted
applications.

%prep
%setup -q -n txAMQP-%{version}
# Fix non-executable-script error
sed -i '/^#!\/usr\/bin\/env python/,+1 d' src/txamqp/codec.py

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{upstream_name}
%doc LICENSE
%{python3_sitelib}/%{upstream_name}
%exclude %{python3_sitelib}/%{upstream_name}/contrib/thrift
%{python3_sitelib}/txAMQP-%{version}-*.egg-info

%files -n python3-%{upstream_name}-thrift
%{python3_sitelib}/%{upstream_name}/contrib/thrift

%changelog
* Fri Feb 12 2021 Francois Poirotte <francois.poirotte@c-s.fr> - 0.8.2-1
- Build for rawhide and EL8
