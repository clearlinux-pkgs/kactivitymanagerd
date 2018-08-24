#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kactivitymanagerd
Version  : 5.13.4
Release  : 1
URL      : https://download.kde.org/stable/plasma/5.13.4/kactivitymanagerd-5.13.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.13.4/kactivitymanagerd-5.13.4.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.13.4/kactivitymanagerd-5.13.4.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: kactivitymanagerd-bin
Requires: kactivitymanagerd-lib
Requires: kactivitymanagerd-data
Requires: kactivitymanagerd-license
Requires: kactivitymanagerd-locales
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kwindowsystem-dev

%description
Compiler compatibility
======================
You can (and should) use more modern C++ coding practices. Including
auto, lambdas, smart pointers etc. You can use anything that GCC 4.7
can compile.

%package bin
Summary: bin components for the kactivitymanagerd package.
Group: Binaries
Requires: kactivitymanagerd-data
Requires: kactivitymanagerd-license

%description bin
bin components for the kactivitymanagerd package.


%package data
Summary: data components for the kactivitymanagerd package.
Group: Data

%description data
data components for the kactivitymanagerd package.


%package dev
Summary: dev components for the kactivitymanagerd package.
Group: Development
Requires: kactivitymanagerd-lib
Requires: kactivitymanagerd-bin
Requires: kactivitymanagerd-data
Provides: kactivitymanagerd-devel

%description dev
dev components for the kactivitymanagerd package.


%package lib
Summary: lib components for the kactivitymanagerd package.
Group: Libraries
Requires: kactivitymanagerd-data
Requires: kactivitymanagerd-license

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
%setup -q -n kactivitymanagerd-5.13.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535147417
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535147417
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kactivitymanagerd
cp COPYING.GPL2 %{buildroot}/usr/share/doc/kactivitymanagerd/COPYING.GPL2
cp COPYING.GPL3 %{buildroot}/usr/share/doc/kactivitymanagerd/COPYING.GPL3
pushd clr-build
%make_install
popd
%find_lang kactivities5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kactivitymanagerd

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.kde.activitymanager.service
/usr/share/kservices5/kactivitymanagerd.desktop
/usr/share/kservicetypes5/kactivitymanagerd-plugin.desktop

%files dev
%defattr(-,root,root,-)
/usr/lib64/libkactivitymanagerd_plugin.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activitytemplates.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_eventspy.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_globalshortcuts.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_runapplication.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_slc.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_sqlite.so
/usr/lib64/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_virtualdesktopswitch.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/kactivitymanagerd/COPYING.GPL2
/usr/share/doc/kactivitymanagerd/COPYING.GPL3

%files locales -f kactivities5.lang
%defattr(-,root,root,-)

