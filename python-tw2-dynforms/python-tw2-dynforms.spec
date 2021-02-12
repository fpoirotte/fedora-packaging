%global modname tw2.dynforms

Name:           python-tw2-dynforms
Version:        2.0.1
Release:        20%{?dist}
Summary:        Dynamic widgets with JavaScript for ToscaWidgets 2

License:        MIT
URL:            http://toscawidgets.org
Source0:        https://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
Patch0:         python-tw2-dynforms-setup.diff
Patch1:         python-tw2-dynforms-relative-imports.diff
Patch2:         python-tw2-dynforms-modname.diff
BuildArch:      noarch

# For building
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-genshi
BuildRequires:  python3-tw2-core
BuildRequires:  python3-tw2-forms

# For the test suite
BuildRequires:  python3-formencode
BuildRequires:  python3-nose
BuildRequires:  python3-sieve
BuildRequires:  python3-webtest

%global _description\
ToscaWidgets is a web widget toolkit for Python to aid in the creation,\
packaging and distribution of common view elements normally used in the web.\
\
tw2.dynforms includes dynamic form building widgets that use JavaScript.

%description %_description

%package -n python3-tw2-dynforms
Summary:        %summary
Requires:       python3dist(genshi)
Requires:       python3dist(tw2.core)
Requires:       python3dist(tw2.forms)
%{?python_provide:%python_provide python3-tw2-dynforms}

%description -n python3-tw2-dynforms %_description

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1 -b .setup
%patch1 -p1 -b .relimport
%patch2 -p1 -b .modname

# Remove pre-compiled files
find tw2/ '(' -name '*.pyc' -o -name '*.pyo' ')' -delete

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%check
# nose gets confused due to the use of namespaces
rm tw2/__init__.py
PYTHONPATH=$(pwd) %{__python3} setup.py test

%files -n python3-tw2-dynforms
%license LICENSE
%doc README.rst
%{python3_sitelib}/tw2/dynforms
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Thu Feb 11 2021 François Poirotte <francois.poirotte@csnovidys.com> - 2.0.1-20
- Removed support for Python 2
- Added support for Python 3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.1-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.1-15
- Python 2 binary package renamed to python2-tw2-dynforms
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 13 2014 Ralph Bean <rbean@redhat.com> - 2.0.1-9
- Fix rhel conditional.

* Thu Jun 12 2014 Ralph Bean <rbean@redhat.com> - 2.0.1-8
- Add dep on python-sieve.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-3
- Fixed (again) incorrect directory ownership.

* Thu May 03 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-2
- Fixed incoherent-version-in-changelog.
- Fixed directory ownership issue.

* Wed May 02 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-1
- New upstream release.  Contains license file.

* Wed May 02 2012 Ralph Bean <rbean@redhat.com> - 2.0.0-2
- Removed clean section
- Removed defattr in files section
- Removed unnecessary references to buildroot

* Wed Apr 11 2012 Ralph Bean <rbean@redhat.com> - 2.0.0-1
- Initial packaging for Fedora
