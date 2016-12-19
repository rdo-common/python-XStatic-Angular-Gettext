%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name XStatic-Angular-Gettext

Name:           python-%{pypi_name}
Version:        2.1.0.2
Release:        5%{?dist}
Summary:        Angular-Gettext (XStatic packaging standard)

License:        MIT
URL:            https://angular-gettext.rocketeer.be/
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n python2-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires:       python2-XStatic
Requires:       xstatic-angular-gettext-common

%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 2 build of %{pypi_name}.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-angular-gettext-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.
%endif

%package -n xstatic-angular-gettext-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-angular-gettext-common
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the javascript files.

%prep
%autosetup -n %{pypi_name}-%{version}
# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_gettext'|" xstatic/pkg/angular_gettext/__init__.py

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
mkdir -p %{buildroot}%{_jsdir}/angular_gettext
mv %{buildroot}%{python2_sitelib}/xstatic/pkg/angular_gettext/data/angular-gettext.js %{buildroot}%{_jsdir}/angular_gettext
rmdir %{buildroot}%{python2_sitelib}/xstatic/pkg/angular_gettext/data/
# fix execute flags for js
chmod 644 %{buildroot}%{_jsdir}/angular_gettext/angular-gettext.js

%if 0%{?with_python3}
%py3_install
# Remove static files, already created by the python2 subpkg
rm -rf %{buildroot}%{python3_sitelib}/xstatic/pkg/angular_gettext/data
%endif

%files -n python2-%{pypi_name}
%doc README.txt
%{python2_sitelib}/xstatic/pkg/angular_gettext
%{python2_sitelib}/XStatic_Angular_Gettext-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/XStatic_Angular_Gettext-%{version}-py%{python2_version}-nspkg.pth

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/angular_gettext
%{python3_sitelib}/XStatic_Angular_Gettext-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_Angular_Gettext-%{version}-py%{python3_version}-nspkg.pth
%endif

%files -n xstatic-angular-gettext-common
%doc README.txt
%{_jsdir}/angular_gettext

%changelog
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.0.2-5
- Rebuild for Python 3.6

* Fri Oct 07 2016 Jan Beran <jberan@redhat.com> - 2.1.0.2-4
- Provides a Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 06 2015 Matthias Runge <mrunge@redhat.com> - 2.1.0.2-1
- Initial package (rhbz#1250929)

