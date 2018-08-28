#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kpackage
Version  : 5.49.0
Release  : 3
URL      : https://download.kde.org/stable/frameworks/5.49/kpackage-5.49.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.49/kpackage-5.49.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.49/kpackage-5.49.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kpackage-bin
Requires: kpackage-lib
Requires: kpackage-license
Requires: kpackage-data
Requires: kpackage-locales
Requires: kpackage-man
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : karchive-dev
BuildRequires : kdoctools
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
# KPackage Framework
Installation and loading of additional content (ex: scripts, images...) as packages

%package bin
Summary: bin components for the kpackage package.
Group: Binaries
Requires: kpackage-data
Requires: kpackage-license
Requires: kpackage-man

%description bin
bin components for the kpackage package.


%package data
Summary: data components for the kpackage package.
Group: Data

%description data
data components for the kpackage package.


%package dev
Summary: dev components for the kpackage package.
Group: Development
Requires: kpackage-lib
Requires: kpackage-bin
Requires: kpackage-data
Provides: kpackage-devel

%description dev
dev components for the kpackage package.


%package lib
Summary: lib components for the kpackage package.
Group: Libraries
Requires: kpackage-data
Requires: kpackage-license

%description lib
lib components for the kpackage package.


%package license
Summary: license components for the kpackage package.
Group: Default

%description license
license components for the kpackage package.


%package locales
Summary: locales components for the kpackage package.
Group: Default

%description locales
locales components for the kpackage package.


%package man
Summary: man components for the kpackage package.
Group: Default

%description man
man components for the kpackage package.


%prep
%setup -q -n kpackage-5.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535431843
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535431843
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kpackage
cp COPYING %{buildroot}/usr/share/doc/kpackage/COPYING
cp COPYING.LIB %{buildroot}/usr/share/doc/kpackage/COPYING.LIB
cp src/kpackage/COPYING.LIB %{buildroot}/usr/share/doc/kpackage/src_kpackage_COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libkpackage5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kpackagetool5

%files data
%defattr(-,root,root,-)
/usr/share/kservicetypes5/kpackage-generic.desktop
/usr/share/kservicetypes5/kpackage-genericqml.desktop
/usr/share/kservicetypes5/kpackage-packagestructure.desktop
/usr/share/xdg/kpackage.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KPackage/KPackage/Package
/usr/include/KF5/KPackage/KPackage/PackageLoader
/usr/include/KF5/KPackage/KPackage/PackageStructure
/usr/include/KF5/KPackage/kpackage/package.h
/usr/include/KF5/KPackage/kpackage/package_export.h
/usr/include/KF5/KPackage/kpackage/packageloader.h
/usr/include/KF5/KPackage/kpackage/packagestructure.h
/usr/include/KF5/KPackage/kpackage/version.h
/usr/include/KF5/kpackage_version.h
/usr/lib64/cmake/KF5Package/KF5PackageConfig.cmake
/usr/lib64/cmake/KF5Package/KF5PackageConfigVersion.cmake
/usr/lib64/cmake/KF5Package/KF5PackageMacros.cmake
/usr/lib64/cmake/KF5Package/KF5PackageTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Package/KF5PackageTargets.cmake
/usr/lib64/cmake/KF5Package/qrc.cmake
/usr/lib64/libKF5Package.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Package.so.5
/usr/lib64/libKF5Package.so.5.49.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/kpackage/COPYING
/usr/share/doc/kpackage/COPYING.LIB
/usr/share/doc/kpackage/src_kpackage_COPYING.LIB

%files man
%defattr(-,root,root,-)
/usr/share/man/ca/man1/kpackagetool5.1
/usr/share/man/de/man1/kpackagetool5.1
/usr/share/man/es/man1/kpackagetool5.1
/usr/share/man/it/man1/kpackagetool5.1
/usr/share/man/man1/kpackagetool5.1
/usr/share/man/nl/man1/kpackagetool5.1
/usr/share/man/pt/man1/kpackagetool5.1
/usr/share/man/pt_BR/man1/kpackagetool5.1
/usr/share/man/sv/man1/kpackagetool5.1
/usr/share/man/uk/man1/kpackagetool5.1

%files locales -f libkpackage5.lang
%defattr(-,root,root,-)

