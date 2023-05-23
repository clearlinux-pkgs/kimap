#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
%define keepstatic 1
Name     : kimap
Version  : 23.04.1
Release  : 65
URL      : https://download.kde.org/stable/release-service/23.04.1/src/kimap-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/kimap-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/kimap-23.04.1.tar.xz.sig
Summary  : Job-based API for interacting with IMAP servers
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: kimap-data = %{version}-%{release}
Requires: kimap-lib = %{version}-%{release}
Requires: kimap-license = %{version}-%{release}
Requires: kimap-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : extra-cmake-modules-data
BuildRequires : kmime-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

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
Requires: kimap-staticdev

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

%description staticdev
staticdev components for the kimap package.


%prep
%setup -q -n kimap-23.04.1
cd %{_builddir}/kimap-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684862334
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1684862334
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kimap
cp %{_builddir}/kimap-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/kimap/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kimap-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kimap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kimap-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kimap/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kimap-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kimap/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kimap-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kimap/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kimap-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kimap/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kimap-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kimap/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kimap-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kimap/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libkimap5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kimap.categories
/usr/share/qlogging-categories5/kimap.renamecategories

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5IMAP.so
/usr/include/KPim5/KIMAP/KIMAP/Acl
/usr/include/KPim5/KIMAP/KIMAP/AclJobBase
/usr/include/KPim5/KIMAP/KIMAP/AppendJob
/usr/include/KPim5/KIMAP/KIMAP/CapabilitiesJob
/usr/include/KPim5/KIMAP/KIMAP/CloseJob
/usr/include/KPim5/KIMAP/KIMAP/CopyJob
/usr/include/KPim5/KIMAP/KIMAP/CreateJob
/usr/include/KPim5/KIMAP/KIMAP/DeleteAclJob
/usr/include/KPim5/KIMAP/KIMAP/DeleteJob
/usr/include/KPim5/KIMAP/KIMAP/EnableJob
/usr/include/KPim5/KIMAP/KIMAP/ExpungeJob
/usr/include/KPim5/KIMAP/KIMAP/FetchJob
/usr/include/KPim5/KIMAP/KIMAP/GetAclJob
/usr/include/KPim5/KIMAP/KIMAP/GetMetaDataJob
/usr/include/KPim5/KIMAP/KIMAP/GetQuotaJob
/usr/include/KPim5/KIMAP/KIMAP/GetQuotaRootJob
/usr/include/KPim5/KIMAP/KIMAP/IdJob
/usr/include/KPim5/KIMAP/KIMAP/IdleJob
/usr/include/KPim5/KIMAP/KIMAP/ImapSet
/usr/include/KPim5/KIMAP/KIMAP/Job
/usr/include/KPim5/KIMAP/KIMAP/ListJob
/usr/include/KPim5/KIMAP/KIMAP/ListRightsJob
/usr/include/KPim5/KIMAP/KIMAP/LoginJob
/usr/include/KPim5/KIMAP/KIMAP/LogoutJob
/usr/include/KPim5/KIMAP/KIMAP/MetaDataJobBase
/usr/include/KPim5/KIMAP/KIMAP/MoveJob
/usr/include/KPim5/KIMAP/KIMAP/MyRightsJob
/usr/include/KPim5/KIMAP/KIMAP/NamespaceJob
/usr/include/KPim5/KIMAP/KIMAP/QuotaJobBase
/usr/include/KPim5/KIMAP/KIMAP/RFCCodecs
/usr/include/KPim5/KIMAP/KIMAP/RenameJob
/usr/include/KPim5/KIMAP/KIMAP/SearchJob
/usr/include/KPim5/KIMAP/KIMAP/SelectJob
/usr/include/KPim5/KIMAP/KIMAP/Session
/usr/include/KPim5/KIMAP/KIMAP/SessionUiProxy
/usr/include/KPim5/KIMAP/KIMAP/SetAclJob
/usr/include/KPim5/KIMAP/KIMAP/SetMetaDataJob
/usr/include/KPim5/KIMAP/KIMAP/SetQuotaJob
/usr/include/KPim5/KIMAP/KIMAP/StatusJob
/usr/include/KPim5/KIMAP/KIMAP/StoreJob
/usr/include/KPim5/KIMAP/KIMAP/SubscribeJob
/usr/include/KPim5/KIMAP/KIMAP/UnsubscribeJob
/usr/include/KPim5/KIMAP/kimap/Acl
/usr/include/KPim5/KIMAP/kimap/AclJobBase
/usr/include/KPim5/KIMAP/kimap/AppendJob
/usr/include/KPim5/KIMAP/kimap/CapabilitiesJob
/usr/include/KPim5/KIMAP/kimap/CloseJob
/usr/include/KPim5/KIMAP/kimap/CopyJob
/usr/include/KPim5/KIMAP/kimap/CreateJob
/usr/include/KPim5/KIMAP/kimap/DeleteAclJob
/usr/include/KPim5/KIMAP/kimap/DeleteJob
/usr/include/KPim5/KIMAP/kimap/EnableJob
/usr/include/KPim5/KIMAP/kimap/ExpungeJob
/usr/include/KPim5/KIMAP/kimap/FetchJob
/usr/include/KPim5/KIMAP/kimap/GetAclJob
/usr/include/KPim5/KIMAP/kimap/GetMetaDataJob
/usr/include/KPim5/KIMAP/kimap/GetQuotaJob
/usr/include/KPim5/KIMAP/kimap/GetQuotaRootJob
/usr/include/KPim5/KIMAP/kimap/IdJob
/usr/include/KPim5/KIMAP/kimap/IdleJob
/usr/include/KPim5/KIMAP/kimap/ImapSet
/usr/include/KPim5/KIMAP/kimap/Job
/usr/include/KPim5/KIMAP/kimap/ListJob
/usr/include/KPim5/KIMAP/kimap/ListRightsJob
/usr/include/KPim5/KIMAP/kimap/LoginJob
/usr/include/KPim5/KIMAP/kimap/LogoutJob
/usr/include/KPim5/KIMAP/kimap/MetaDataJobBase
/usr/include/KPim5/KIMAP/kimap/MoveJob
/usr/include/KPim5/KIMAP/kimap/MyRightsJob
/usr/include/KPim5/KIMAP/kimap/NamespaceJob
/usr/include/KPim5/KIMAP/kimap/QuotaJobBase
/usr/include/KPim5/KIMAP/kimap/RFCCodecs
/usr/include/KPim5/KIMAP/kimap/RenameJob
/usr/include/KPim5/KIMAP/kimap/SearchJob
/usr/include/KPim5/KIMAP/kimap/SelectJob
/usr/include/KPim5/KIMAP/kimap/Session
/usr/include/KPim5/KIMAP/kimap/SessionUiProxy
/usr/include/KPim5/KIMAP/kimap/SetAclJob
/usr/include/KPim5/KIMAP/kimap/SetMetaDataJob
/usr/include/KPim5/KIMAP/kimap/SetQuotaJob
/usr/include/KPim5/KIMAP/kimap/StatusJob
/usr/include/KPim5/KIMAP/kimap/StoreJob
/usr/include/KPim5/KIMAP/kimap/SubscribeJob
/usr/include/KPim5/KIMAP/kimap/UnsubscribeJob
/usr/include/KPim5/KIMAP/kimap/acl.h
/usr/include/KPim5/KIMAP/kimap/acljobbase.h
/usr/include/KPim5/KIMAP/kimap/appendjob.h
/usr/include/KPim5/KIMAP/kimap/capabilitiesjob.h
/usr/include/KPim5/KIMAP/kimap/closejob.h
/usr/include/KPim5/KIMAP/kimap/copyjob.h
/usr/include/KPim5/KIMAP/kimap/createjob.h
/usr/include/KPim5/KIMAP/kimap/deleteacljob.h
/usr/include/KPim5/KIMAP/kimap/deletejob.h
/usr/include/KPim5/KIMAP/kimap/enablejob.h
/usr/include/KPim5/KIMAP/kimap/expungejob.h
/usr/include/KPim5/KIMAP/kimap/fetchjob.h
/usr/include/KPim5/KIMAP/kimap/getacljob.h
/usr/include/KPim5/KIMAP/kimap/getmetadatajob.h
/usr/include/KPim5/KIMAP/kimap/getquotajob.h
/usr/include/KPim5/KIMAP/kimap/getquotarootjob.h
/usr/include/KPim5/KIMAP/kimap/idjob.h
/usr/include/KPim5/KIMAP/kimap/idlejob.h
/usr/include/KPim5/KIMAP/kimap/imapset.h
/usr/include/KPim5/KIMAP/kimap/job.h
/usr/include/KPim5/KIMAP/kimap/kimap_export.h
/usr/include/KPim5/KIMAP/kimap/listjob.h
/usr/include/KPim5/KIMAP/kimap/listrightsjob.h
/usr/include/KPim5/KIMAP/kimap/loginjob.h
/usr/include/KPim5/KIMAP/kimap/logoutjob.h
/usr/include/KPim5/KIMAP/kimap/metadatajobbase.h
/usr/include/KPim5/KIMAP/kimap/movejob.h
/usr/include/KPim5/KIMAP/kimap/myrightsjob.h
/usr/include/KPim5/KIMAP/kimap/namespacejob.h
/usr/include/KPim5/KIMAP/kimap/quotajobbase.h
/usr/include/KPim5/KIMAP/kimap/renamejob.h
/usr/include/KPim5/KIMAP/kimap/rfccodecs.h
/usr/include/KPim5/KIMAP/kimap/searchjob.h
/usr/include/KPim5/KIMAP/kimap/selectjob.h
/usr/include/KPim5/KIMAP/kimap/session.h
/usr/include/KPim5/KIMAP/kimap/sessionuiproxy.h
/usr/include/KPim5/KIMAP/kimap/setacljob.h
/usr/include/KPim5/KIMAP/kimap/setmetadatajob.h
/usr/include/KPim5/KIMAP/kimap/setquotajob.h
/usr/include/KPim5/KIMAP/kimap/statusjob.h
/usr/include/KPim5/KIMAP/kimap/storejob.h
/usr/include/KPim5/KIMAP/kimap/subscribejob.h
/usr/include/KPim5/KIMAP/kimap/unsubscribejob.h
/usr/include/KPim5/KIMAP/kimap_version.h
/usr/include/KPim5/KIMAPTest/kimaptest/fakeserver.h
/usr/include/KPim5/KIMAPTest/kimaptest/mockjob.h
/usr/lib64/cmake/KF5IMAP/KF5IMAPConfig.cmake
/usr/lib64/cmake/KF5IMAP/KF5IMAPConfigVersion.cmake
/usr/lib64/cmake/KF5IMAP/KPim5IMAPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5IMAP/KPim5IMAPTargets.cmake
/usr/lib64/cmake/KPim5IMAP/KPim5IMAPConfig.cmake
/usr/lib64/cmake/KPim5IMAP/KPim5IMAPConfigVersion.cmake
/usr/lib64/cmake/KPim5IMAP/KPim5IMAPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5IMAP/KPim5IMAPTargets.cmake
/usr/lib64/libKPim5IMAP.so
/usr/lib64/qt5/mkspecs/modules/qt_KIMAP.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5IMAP.so.5
/V3/usr/lib64/libKPim5IMAP.so.5.23.1
/usr/lib64/libKPim5IMAP.so.5
/usr/lib64/libKPim5IMAP.so.5.23.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kimap/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kimap/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kimap/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kimap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kimap/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libkimaptest.a

%files locales -f libkimap5.lang
%defattr(-,root,root,-)

