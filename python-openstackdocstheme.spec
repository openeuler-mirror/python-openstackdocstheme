%global _empty_manifest_terminate_build 0
Name:		python-openstackdocstheme
Version:	1.18.1
Release:	2
Summary:	OpenStack Docs Theme
License:	Apache-2.0
URL:		https://docs.openstack.org/openstackdocstheme/latest/
Source0:	https://files.pythonhosted.org/packages/83/5b/cd40d2c49ce828f265d99f8cb1b409851ac010f101e774f981920b68c9f6/openstackdocstheme-1.18.1.tar.gz
BuildArch:	noarch
%description
 Team and repository tags .. Change things from this point onOpenStack
docs.openstack.org Sphinx Theme Theme and extension support for Sphinx
documentation that is published to docs.openstack.org and
developer.openstack.org.Intended for use by OpenStack projects governed by the
Technical Committee... _projects governed by the Technical Committee:

%package -n python2-openstackdocstheme
Summary:	OpenStack Docs Theme
Provides:	python2-openstackdocstheme
BuildRequires:	python2-pbr
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
Requires:	python2-pbr
Requires:	python2-dulwich
%description -n python2-openstackdocstheme
 Team and repository tags .. Change things from this point onOpenStack
docs.openstack.org Sphinx Theme Theme and extension support for Sphinx
documentation that is published to docs.openstack.org and
developer.openstack.org.Intended for use by OpenStack projects governed by the
Technical Committee... _projects governed by the Technical Committee:

%package help
Summary:	Development documents and examples for openstackdocstheme
Provides:	python2-openstackdocstheme-doc
%description help
 Team and repository tags .. Change things from this point onOpenStack
docs.openstack.org Sphinx Theme Theme and extension support for Sphinx
documentation that is published to docs.openstack.org and
developer.openstack.org.Intended for use by OpenStack projects governed by the
Technical Committee... _projects governed by the Technical Committee:

%prep
%autosetup -n openstackdocstheme-1.18.1

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
* Fri Sep 10 2021 huangtianhua <huangtianhua@huawei.com> - 1.18.1-2
- Adds python2-pbr as BuildRequires

* Wed May 12 2021 OpenStack_SIG <openstack@openeuler.org>
- Package Spec generated
