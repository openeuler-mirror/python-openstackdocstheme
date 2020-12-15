%global _empty_manifest_terminate_build 0
Name:		python-openstackdocstheme
Version:	2.2.6
Release:	1
Summary:	OpenStack Docs Theme
License:	Apache-2.0
URL:		https://docs.openstack.org/openstackdocstheme/latest/
Source0:	https://files.pythonhosted.org/packages/fc/41/024963ee03015130ef7d4514f526c921da559d65f9c41f7f416891cfae2e/openstackdocstheme-2.2.6.tar.gz
BuildArch:	noarch

Requires:	python3-dulwich
Requires:	python3-pbr

%description
Theme and extension support for Sphinx documentation that is published by Open Infrastructure Foundation projects.

%package -n python3-openstackdocstheme
Summary:	OpenStack Docs Theme
Provides:	python-openstackdocstheme
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-openstackdocstheme


%package help
Summary:	Development documents and examples for openstackdocstheme
Provides:	python3-openstackdocstheme-doc
%description help


%prep
%autosetup -n openstackdocstheme-2.2.6

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-openstackdocstheme -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Nov 20 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
