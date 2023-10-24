#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: 250a666
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kpackage
Version  : 5.111.0
Release  : 205
URL      : https://download.kde.org/stable/frameworks/5.111/kpackage-5.111.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.111/kpackage-5.111.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.111/kpackage-5.111.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0
Requires: kpackage-bin = %{version}-%{release}
Requires: kpackage-data = %{version}-%{release}
Requires: kpackage-lib = %{version}-%{release}
Requires: kpackage-license = %{version}-%{release}
Requires: kpackage-locales = %{version}-%{release}
Requires: kpackage-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : karchive-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KPackage Framework
Installation and loading of additional content (ex: scripts, images...) as packages.

%package bin
Summary: bin components for the kpackage package.
Group: Binaries
Requires: kpackage-data = %{version}-%{release}
Requires: kpackage-license = %{version}-%{release}

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
Requires: kpackage-lib = %{version}-%{release}
Requires: kpackage-bin = %{version}-%{release}
Requires: kpackage-data = %{version}-%{release}
Provides: kpackage-devel = %{version}-%{release}
Requires: kpackage = %{version}-%{release}

%description dev
dev components for the kpackage package.


%package lib
Summary: lib components for the kpackage package.
Group: Libraries
Requires: kpackage-data = %{version}-%{release}
Requires: kpackage-license = %{version}-%{release}

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
%setup -q -n kpackage-5.111.0
cd %{_builddir}/kpackage-5.111.0

%build
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698164074
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1698164074
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpackage
cp %{_builddir}/kpackage-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kpackage/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kpackage-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kpackage/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kpackage-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kpackage/20079e8f79713dce80ab09774505773c926afa2a || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libkpackage5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kpackagetool5
/usr/bin/kpackagetool5

%files data
%defattr(-,root,root,-)
/usr/share/kservicetypes5/kpackage-generic.desktop
/usr/share/kservicetypes5/kpackage-genericqml.desktop
/usr/share/kservicetypes5/kpackage-packagestructure.desktop
/usr/share/qlogging-categories5/kpackage.categories
/usr/share/qlogging-categories5/kpackage.renamecategories

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
/usr/include/KF5/KPackage/kpackage_version.h
/usr/lib64/cmake/KF5Package/KF5PackageConfig.cmake
/usr/lib64/cmake/KF5Package/KF5PackageConfigVersion.cmake
/usr/lib64/cmake/KF5Package/KF5PackageMacros.cmake
/usr/lib64/cmake/KF5Package/KF5PackageTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Package/KF5PackageTargets.cmake
/usr/lib64/cmake/KF5Package/KF5PackageToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Package/KF5PackageToolsTargets.cmake
/usr/lib64/cmake/KF5Package/qrc.cmake
/usr/lib64/libKF5Package.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Package.so.5.111.0
/usr/lib64/libKF5Package.so.5
/usr/lib64/libKF5Package.so.5.111.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpackage/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kpackage/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kpackage/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kpackagetool5.1
/usr/share/man/ca@valencia/man1/kpackagetool5.1
/usr/share/man/de/man1/kpackagetool5.1
/usr/share/man/es/man1/kpackagetool5.1
/usr/share/man/fr/man1/kpackagetool5.1
/usr/share/man/it/man1/kpackagetool5.1
/usr/share/man/man1/kpackagetool5.1
/usr/share/man/nl/man1/kpackagetool5.1
/usr/share/man/pt/man1/kpackagetool5.1
/usr/share/man/pt_BR/man1/kpackagetool5.1
/usr/share/man/sv/man1/kpackagetool5.1
/usr/share/man/uk/man1/kpackagetool5.1

%files locales -f libkpackage5.lang
%defattr(-,root,root,-)

