%global _empty_manifest_terminate_build 0
Name:		python-openstackdocstheme
Version:	1.20.1
Release:	2
Summary:	OpenStack Docs Theme
License:	Apache-2.0, CC-BY-3.0
URL:		https://docs.openstack.org/openstackdocstheme/latest/
Source0:	https://files.pythonhosted.org/packages/2d/5c/166e3950c7c9ba6fc2500e6ba40e92fe0b5c19c6c839b14ff01d8366e5b7/openstackdocstheme-1.20.1.tar.gz
BuildArch:	noarch

Requires:	python2-pbr
Requires:	python2-dulwich

%description


%package -n python2-openstackdocstheme
Summary:	OpenStack Docs Theme
Provides:	python2-openstackdocstheme
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:	python2-pbr

%description -n python2-openstackdocstheme


%package help
Summary:	Development documents and examples for openstackdocstheme
Provides:	python2-openstackdocstheme-doc
%description help


%prep
%autosetup -n openstackdocstheme-1.20.1

%build
%py2_build

%install
%py2_install
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

%files -n python2-openstackdocstheme -f filelist.lst
%dir %{python2_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue Nov 23 huangtianhua <huangtianhua@huawei.com> - 1.20.1-2
- Adds python2-pbr as BuildRequires and correct provides

* Mon May 10 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
