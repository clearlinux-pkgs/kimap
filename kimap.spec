#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
%define keepstatic 1
Name     : kimap
Version  : 19.12.3
Release  : 24
URL      : https://download.kde.org/stable/release-service/19.12.3/src/kimap-19.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.3/src/kimap-19.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.3/src/kimap-19.12.3.tar.xz.sig
Summary  : Job-based API for interacting with IMAP servers
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kimap-data = %{version}-%{release}
Requires: kimap-lib = %{version}-%{release}
Requires: kimap-license = %{version}-%{release}
Requires: kimap-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : kmime-dev
BuildRequires : qtbase-dev mesa-dev

%description
# KIMAP #
This library provides a job-based API for interacting with an IMAP4rev1 server.
It manages connections, encryption and parameter quoting and encoding, but
otherwise provides quite a low-level interface to the protocol.  This library
does not implement an IMAP client; it merely makes it easier to do so.

%package data
Summary: data components for the kimap package.
Group: Data

%description data
data components for the kimap package.


%package dev
Summary: dev components for the kimap package.
Group: Development
Requires: kimap-lib = %{version}-%{release}
Requires: kimap-data = %{version}-%{release}
Provides: kimap-devel = %{version}-%{release}
Requires: kimap = %{version}-%{release}
Requires: kimap = %{version}-%{release}

%description dev
dev components for the kimap package.


%package lib
Summary: lib components for the kimap package.
Group: Libraries
Requires: kimap-data = %{version}-%{release}
Requires: kimap-license = %{version}-%{release}

%description lib
lib components for the kimap package.


%package license
Summary: license components for the kimap package.
Group: Default

%description license
license components for the kimap package.


%package locales
Summary: locales components for the kimap package.
Group: Default

%description locales
locales components for the kimap package.


%package staticdev
Summary: staticdev components for the kimap package.
Group: Default
Requires: kimap-dev = %{version}-%{release}
Requires: kimap-dev = %{version}-%{release}

%description staticdev
staticdev components for the kimap package.


%prep
%setup -q -n kimap-19.12.3
cd %{_builddir}/kimap-19.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583506412
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
export SOURCE_DATE_EPOCH=1583506412
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kimap
cp %{_builddir}/kimap-19.12.3/COPYING %{buildroot}/usr/share/package-licenses/kimap/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/kimap-19.12.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/kimap/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang libkimap5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kimap.categories
/usr/share/qlogging-categories5/kimap.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KIMAP/KIMAP/Acl
/usr/include/KF5/KIMAP/KIMAP/AclJobBase
/usr/include/KF5/KIMAP/KIMAP/AppendJob
/usr/include/KF5/KIMAP/KIMAP/CapabilitiesJob
/usr/include/KF5/KIMAP/KIMAP/CloseJob
/usr/include/KF5/KIMAP/KIMAP/CopyJob
/usr/include/KF5/KIMAP/KIMAP/CreateJob
/usr/include/KF5/KIMAP/KIMAP/DeleteAclJob
/usr/include/KF5/KIMAP/KIMAP/DeleteJob
/usr/include/KF5/KIMAP/KIMAP/ExpungeJob
/usr/include/KF5/KIMAP/KIMAP/FetchJob
/usr/include/KF5/KIMAP/KIMAP/GetAclJob
/usr/include/KF5/KIMAP/KIMAP/GetMetaDataJob
/usr/include/KF5/KIMAP/KIMAP/GetQuotaJob
/usr/include/KF5/KIMAP/KIMAP/GetQuotaRootJob
/usr/include/KF5/KIMAP/KIMAP/IdJob
/usr/include/KF5/KIMAP/KIMAP/IdleJob
/usr/include/KF5/KIMAP/KIMAP/ImapSet
/usr/include/KF5/KIMAP/KIMAP/Job
/usr/include/KF5/KIMAP/KIMAP/ListJob
/usr/include/KF5/KIMAP/KIMAP/ListRightsJob
/usr/include/KF5/KIMAP/KIMAP/LoginJob
/usr/include/KF5/KIMAP/KIMAP/LogoutJob
/usr/include/KF5/KIMAP/KIMAP/MetaDataJobBase
/usr/include/KF5/KIMAP/KIMAP/MoveJob
/usr/include/KF5/KIMAP/KIMAP/MyRightsJob
/usr/include/KF5/KIMAP/KIMAP/NamespaceJob
/usr/include/KF5/KIMAP/KIMAP/QuotaJobBase
/usr/include/KF5/KIMAP/KIMAP/RFCCodecs
/usr/include/KF5/KIMAP/KIMAP/RenameJob
/usr/include/KF5/KIMAP/KIMAP/SearchJob
/usr/include/KF5/KIMAP/KIMAP/SelectJob
/usr/include/KF5/KIMAP/KIMAP/Session
/usr/include/KF5/KIMAP/KIMAP/SessionUiProxy
/usr/include/KF5/KIMAP/KIMAP/SetAclJob
/usr/include/KF5/KIMAP/KIMAP/SetMetaDataJob
/usr/include/KF5/KIMAP/KIMAP/SetQuotaJob
/usr/include/KF5/KIMAP/KIMAP/StatusJob
/usr/include/KF5/KIMAP/KIMAP/StoreJob
/usr/include/KF5/KIMAP/KIMAP/SubscribeJob
/usr/include/KF5/KIMAP/KIMAP/UnsubscribeJob
/usr/include/KF5/KIMAP/kimap/Acl
/usr/include/KF5/KIMAP/kimap/AclJobBase
/usr/include/KF5/KIMAP/kimap/AppendJob
/usr/include/KF5/KIMAP/kimap/CapabilitiesJob
/usr/include/KF5/KIMAP/kimap/CloseJob
/usr/include/KF5/KIMAP/kimap/CopyJob
/usr/include/KF5/KIMAP/kimap/CreateJob
/usr/include/KF5/KIMAP/kimap/DeleteAclJob
/usr/include/KF5/KIMAP/kimap/DeleteJob
/usr/include/KF5/KIMAP/kimap/ExpungeJob
/usr/include/KF5/KIMAP/kimap/FetchJob
/usr/include/KF5/KIMAP/kimap/GetAclJob
/usr/include/KF5/KIMAP/kimap/GetMetaDataJob
/usr/include/KF5/KIMAP/kimap/GetQuotaJob
/usr/include/KF5/KIMAP/kimap/GetQuotaRootJob
/usr/include/KF5/KIMAP/kimap/IdJob
/usr/include/KF5/KIMAP/kimap/IdleJob
/usr/include/KF5/KIMAP/kimap/ImapSet
/usr/include/KF5/KIMAP/kimap/Job
/usr/include/KF5/KIMAP/kimap/ListJob
/usr/include/KF5/KIMAP/kimap/ListRightsJob
/usr/include/KF5/KIMAP/kimap/LoginJob
/usr/include/KF5/KIMAP/kimap/LogoutJob
/usr/include/KF5/KIMAP/kimap/MetaDataJobBase
/usr/include/KF5/KIMAP/kimap/MoveJob
/usr/include/KF5/KIMAP/kimap/MyRightsJob
/usr/include/KF5/KIMAP/kimap/NamespaceJob
/usr/include/KF5/KIMAP/kimap/QuotaJobBase
/usr/include/KF5/KIMAP/kimap/RFCCodecs
/usr/include/KF5/KIMAP/kimap/RenameJob
/usr/include/KF5/KIMAP/kimap/SearchJob
/usr/include/KF5/KIMAP/kimap/SelectJob
/usr/include/KF5/KIMAP/kimap/Session
/usr/include/KF5/KIMAP/kimap/SessionUiProxy
/usr/include/KF5/KIMAP/kimap/SetAclJob
/usr/include/KF5/KIMAP/kimap/SetMetaDataJob
/usr/include/KF5/KIMAP/kimap/SetQuotaJob
/usr/include/KF5/KIMAP/kimap/StatusJob
/usr/include/KF5/KIMAP/kimap/StoreJob
/usr/include/KF5/KIMAP/kimap/SubscribeJob
/usr/include/KF5/KIMAP/kimap/UnsubscribeJob
/usr/include/KF5/KIMAP/kimap/acl.h
/usr/include/KF5/KIMAP/kimap/acljobbase.h
/usr/include/KF5/KIMAP/kimap/appendjob.h
/usr/include/KF5/KIMAP/kimap/capabilitiesjob.h
/usr/include/KF5/KIMAP/kimap/closejob.h
/usr/include/KF5/KIMAP/kimap/copyjob.h
/usr/include/KF5/KIMAP/kimap/createjob.h
/usr/include/KF5/KIMAP/kimap/deleteacljob.h
/usr/include/KF5/KIMAP/kimap/deletejob.h
/usr/include/KF5/KIMAP/kimap/expungejob.h
/usr/include/KF5/KIMAP/kimap/fetchjob.h
/usr/include/KF5/KIMAP/kimap/getacljob.h
/usr/include/KF5/KIMAP/kimap/getmetadatajob.h
/usr/include/KF5/KIMAP/kimap/getquotajob.h
/usr/include/KF5/KIMAP/kimap/getquotarootjob.h
/usr/include/KF5/KIMAP/kimap/idjob.h
/usr/include/KF5/KIMAP/kimap/idlejob.h
/usr/include/KF5/KIMAP/kimap/imapset.h
/usr/include/KF5/KIMAP/kimap/job.h
/usr/include/KF5/KIMAP/kimap/kimap_export.h
/usr/include/KF5/KIMAP/kimap/listjob.h
/usr/include/KF5/KIMAP/kimap/listrightsjob.h
/usr/include/KF5/KIMAP/kimap/loginjob.h
/usr/include/KF5/KIMAP/kimap/logoutjob.h
/usr/include/KF5/KIMAP/kimap/metadatajobbase.h
/usr/include/KF5/KIMAP/kimap/movejob.h
/usr/include/KF5/KIMAP/kimap/myrightsjob.h
/usr/include/KF5/KIMAP/kimap/namespacejob.h
/usr/include/KF5/KIMAP/kimap/quotajobbase.h
/usr/include/KF5/KIMAP/kimap/renamejob.h
/usr/include/KF5/KIMAP/kimap/rfccodecs.h
/usr/include/KF5/KIMAP/kimap/searchjob.h
/usr/include/KF5/KIMAP/kimap/selectjob.h
/usr/include/KF5/KIMAP/kimap/session.h
/usr/include/KF5/KIMAP/kimap/sessionuiproxy.h
/usr/include/KF5/KIMAP/kimap/setacljob.h
/usr/include/KF5/KIMAP/kimap/setmetadatajob.h
/usr/include/KF5/KIMAP/kimap/setquotajob.h
/usr/include/KF5/KIMAP/kimap/statusjob.h
/usr/include/KF5/KIMAP/kimap/storejob.h
/usr/include/KF5/KIMAP/kimap/subscribejob.h
/usr/include/KF5/KIMAP/kimap/unsubscribejob.h
/usr/include/KF5/kimap_version.h
/usr/include/KF5/kimaptest/fakeserver.h
/usr/include/KF5/kimaptest/mockjob.h
/usr/lib64/cmake/KF5IMAP/KF5IMAPConfig.cmake
/usr/lib64/cmake/KF5IMAP/KF5IMAPConfigVersion.cmake
/usr/lib64/cmake/KF5IMAP/KF5IMAPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5IMAP/KF5IMAPTargets.cmake
/usr/lib64/libKF5IMAP.so
/usr/lib64/qt5/mkspecs/modules/qt_KIMAP.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5IMAP.so.5
/usr/lib64/libKF5IMAP.so.5.13.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kimap/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/kimap/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libkimaptest.a

%files locales -f libkimap5.lang
%defattr(-,root,root,-)

