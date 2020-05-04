#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : uamqp
Version  : 1.2.7
Release  : 14
URL      : https://files.pythonhosted.org/packages/96/9d/3ccf9a6d0e23201a2920a380ddc0cc7022296a6873264b759758d80c20b6/uamqp-1.2.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/96/9d/3ccf9a6d0e23201a2920a380ddc0cc7022296a6873264b759758d80c20b6/uamqp-1.2.7.tar.gz
Summary  : AMQP 1.0 Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: uamqp-license = %{version}-%{release}
Requires: uamqp-python = %{version}-%{release}
Requires: uamqp-python3 = %{version}-%{release}
Requires: certifi
Requires: six
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : openssl-dev
BuildRequires : python3-dev
BuildRequires : six

%description
================

%package license
Summary: license components for the uamqp package.
Group: Default

%description license
license components for the uamqp package.


%package python
Summary: python components for the uamqp package.
Group: Default
Requires: uamqp-python3 = %{version}-%{release}

%description python
python components for the uamqp package.


%package python3
Summary: python3 components for the uamqp package.
Group: Default
Requires: python3-core
Provides: pypi(uamqp)
Requires: pypi(certifi)
Requires: pypi(six)

%description python3
python3 components for the uamqp package.


%prep
%setup -q -n uamqp-1.2.7
cd %{_builddir}/uamqp-1.2.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588632376
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/uamqp
cp %{_builddir}/uamqp-1.2.7/src/vendor/azure-uamqp-c/LICENSE %{buildroot}/usr/share/package-licenses/uamqp/47e4690f60befa1918e5ac38723973fe4cf04e9b
cp %{_builddir}/uamqp-1.2.7/src/vendor/azure-uamqp-c/build_all/packaging/linux/debian/copyright %{buildroot}/usr/share/package-licenses/uamqp/fcd11f2e53968b872b48efbb6cf2a18c5a0d04e5
cp %{_builddir}/uamqp-1.2.7/src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/LICENSE %{buildroot}/usr/share/package-licenses/uamqp/47e4690f60befa1918e5ac38723973fe4cf04e9b
cp %{_builddir}/uamqp-1.2.7/src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/build_all/packaging/linux/debian/copyright %{buildroot}/usr/share/package-licenses/uamqp/b936129838be63462c2583bfd059d8736f39ab87
cp %{_builddir}/uamqp-1.2.7/src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/testtools/ctest/LICENSE %{buildroot}/usr/share/package-licenses/uamqp/47e4690f60befa1918e5ac38723973fe4cf04e9b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/uamqp/47e4690f60befa1918e5ac38723973fe4cf04e9b
/usr/share/package-licenses/uamqp/b936129838be63462c2583bfd059d8736f39ab87
/usr/share/package-licenses/uamqp/fcd11f2e53968b872b48efbb6cf2a18c5a0d04e5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
