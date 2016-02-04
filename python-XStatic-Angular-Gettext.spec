%global pypi_name XStatic-Angular-Gettext

Name:           python-%{pypi_name}
Version:        2.1.0.2
Release:        2%{?dist}
Summary:        Angular-Gettext (XStatic packaging standard)

License:        MIT
URL:            https://angular-gettext.rocketeer.be/
Source0:        https://pypi.python.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  web-assets-devel

Requires:       python-XStatic
Requires:       web-assets-filesystem

Provides: python2-%{pypi_name} = %{version}-%{release}

%description
Angular-Gettext javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_gettext'|" xstatic/pkg/angular_gettext/__init__.py

%build
# due
# https://bitbucket.org/thomaswaldmann/xstatic/issue/2/
# this package can not be built with python-XStatic installed.
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/%{_jsdir}/angular_gettext
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_gettext/data/angular-gettext.js %{buildroot}/%{_jsdir}/angular_gettext



%files
%doc README.txt
%{python2_sitelib}/xstatic/pkg/angular_gettext
%{python2_sitelib}/XStatic_Angular_Gettext-%{version}-py?.?-nspkg.pth
%{python2_sitelib}/XStatic_Angular_Gettext-%{version}-py?.?.egg-info
%{_jsdir}/angular_gettext

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 06 2015 Matthias Runge <mrunge@redhat.com> - 2.1.0.2-1
- Initial package (rhbz#1250929)
