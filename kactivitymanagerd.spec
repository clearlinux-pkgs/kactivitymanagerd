#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kactivitymanagerd
Version  : 5.27.10
Release  : 87
URL      : https://download.kde.org/stable/plasma/5.27.10/kactivitymanagerd-5.27.10.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.10/kactivitymanagerd-5.27.10.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.10/kactivitymanagerd-5.27.10.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: kactivitymanagerd-data = %{version}-%{release}
Requires: kactivitymanagerd-lib = %{version}-%{release}
Requires: kactivitymanagerd-license = %{version}-%{release}
Requires: kactivitymanagerd-locales = %{version}-%{release}
Requires: kactivitymanagerd-services = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kglobalaccel-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KActivities
Core components for the KDE Activity concept
## Introduction
When a user is interacting with a computer, there are three main areas of
contextual information that may affect the behaviour of the system: who the user
is, where they are, and what they are doing.

%package data
Summary: data components for the kactivitymanagerd package.
Group: Data

%description data
data components for the kactivitymanagerd package.


%package dev
Summary: dev components for the kactivitymanagerd package.
Group: Development
Requires: kactivitymanagerd-lib = %{version}-%{release}
Requires: kactivitymanagerd-data = %{version}-%{release}
Provides: kactivitymanagerd-devel = %{version}-%{release}
Requires: kactivitymanagerd = %{version}-%{release}

%description dev
dev components for the kactivitymanagerd package.


%package lib
Summary: lib components for the kactivitymanagerd package.
Group: Libraries
Requires: kactivitymanagerd-data = %{version}-%{release}
Requires: kactivitymanagerd-license = %{version}-%{release}

%description lib
lib components for the kactivitymanagerd package.


%package license
Summary: license components for the kactivitymanagerd package.
Group: Default

%description license
license components for the kactivitymanagerd package.


%package locales
Summary: locales components for the kactivitymanagerd package.
Group: Default

%description locales
locales components for the kactivitymanagerd package.


%package services
Summary: services components for the kactivitymanagerd package.
Group: Systemd services
Requires: systemd

%description services
services components for the kactivitymanagerd package.


%prep
%setup -q -n kactivitymanagerd-5.27.10
cd %{_builddir}/kactivitymanagerd-5.27.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702990075
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
export SOURCE_DATE_EPOCH=1702990075
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kactivitymanagerd
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kactivitymanagerd-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kactivitymanagerd/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kactivities5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kactivitymanagerd
/usr/lib64/libexec/kactivitymanagerd

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.kde.ActivityManager.service
/usr/share/krunner/dbusplugins/plasma-runnners-activities.desktop
/usr/share/kservices5/kactivitymanagerd.desktop
/usr/share/qlogging-categories5/kactivitymanagerd.categories

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libkactivitymanagerd_plugin.so
/usr/lib64/libkactivitymanagerd_plugin.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activityrunner.so
/V3/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activitytemplates.so
/V3/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_eventspy.so
/V3/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_globalshortcuts.so
/V3/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_gtk_eventspy.so
/V3/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_runapplication.so
/V3/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_slc.so
/V3/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_sqlite.so
/V3/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_virtualdesktopswitch.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activityrunner.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activitytemplates.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_eventspy.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_globalshortcuts.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_gtk_eventspy.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_runapplication.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_slc.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_sqlite.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_virtualdesktopswitch.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kactivitymanagerd/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kactivitymanagerd/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kactivitymanagerd/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kactivitymanagerd/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kactivitymanagerd/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kactivitymanagerd/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kactivitymanagerd/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kactivitymanagerd/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-kactivitymanagerd.service

%files locales -f kactivities5.lang
%defattr(-,root,root,-)

