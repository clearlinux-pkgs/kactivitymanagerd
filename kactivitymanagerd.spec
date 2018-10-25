#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x11968C44928CAEFC (bhush94@gmail.com)
#
Name     : kactivitymanagerd
Version  : 5.14.2
Release  : 5
URL      : https://download.kde.org/stable/plasma/5.14.2/kactivitymanagerd-5.14.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.14.2/kactivitymanagerd-5.14.2.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.14.2/kactivitymanagerd-5.14.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: kactivitymanagerd-bin = %{version}-%{release}
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

%package bin
Summary: bin components for the kactivitymanagerd package.
Group: Binaries
Requires: kactivitymanagerd-data = %{version}-%{release}
Requires: kactivitymanagerd-license = %{version}-%{release}

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
Requires: kactivitymanagerd-lib = %{version}-%{release}
Requires: kactivitymanagerd-bin = %{version}-%{release}
Requires: kactivitymanagerd-data = %{version}-%{release}
Provides: kactivitymanagerd-devel = %{version}-%{release}

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
%setup -q -n kactivitymanagerd-5.14.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540467514
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1540467514
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kactivitymanagerd
cp COPYING.GPL2 %{buildroot}/usr/share/package-licenses/kactivitymanagerd/COPYING.GPL2
cp COPYING.GPL3 %{buildroot}/usr/share/package-licenses/kactivitymanagerd/COPYING.GPL3
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kactivitymanagerd/COPYING.GPL2
/usr/share/package-licenses/kactivitymanagerd/COPYING.GPL3

%files locales -f kactivities5.lang
%defattr(-,root,root,-)

