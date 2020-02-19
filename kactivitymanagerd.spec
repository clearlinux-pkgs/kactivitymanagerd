#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kactivitymanagerd
Version  : 5.18.1
Release  : 30
URL      : https://download.kde.org/stable/plasma/5.18.1/kactivitymanagerd-5.18.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.18.1/kactivitymanagerd-5.18.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.18.1/kactivitymanagerd-5.18.1.tar.xz.sig
Summary  : System service to manage user's activities and track the usage patterns
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: kactivitymanagerd-data = %{version}-%{release}
Requires: kactivitymanagerd-lib = %{version}-%{release}
Requires: kactivitymanagerd-license = %{version}-%{release}
Requires: kactivitymanagerd-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kglobalaccel-dev

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


%prep
%setup -q -n kactivitymanagerd-5.18.1
cd %{_builddir}/kactivitymanagerd-5.18.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582077025
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1582077025
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kactivitymanagerd
cp %{_builddir}/kactivitymanagerd-5.18.1/COPYING.GPL2 %{buildroot}/usr/share/package-licenses/kactivitymanagerd/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kactivitymanagerd-5.18.1/COPYING.GPL3 %{buildroot}/usr/share/package-licenses/kactivitymanagerd/8624bcdae55baeef00cd11d5dfcfa60f68710a02
pushd clr-build
%make_install
popd
%find_lang kactivities5

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kactivitymanagerd

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.kde.activitymanager.service
/usr/share/kservices5/kactivitymanagerd.desktop
/usr/share/kservicetypes5/kactivitymanagerd-plugin.desktop
/usr/share/qlogging-categories5/kactivitymanagerd.categories

%files dev
%defattr(-,root,root,-)
/usr/lib64/libkactivitymanagerd_plugin.so

%files lib
%defattr(-,root,root,-)
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
/usr/share/package-licenses/kactivitymanagerd/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kactivitymanagerd/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files locales -f kactivities5.lang
%defattr(-,root,root,-)

