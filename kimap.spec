#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
%define keepstatic 1
Name     : kimap
Version  : 25.04.2
Release  : 95
URL      : https://download.kde.org/stable/release-service/25.04.2/src/kimap-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/kimap-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/kimap-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Job-based API for interacting with IMAP servers
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: kimap-data = %{version}-%{release}
Requires: kimap-lib = %{version}-%{release}
Requires: kimap-license = %{version}-%{release}
Requires: kimap-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kmime-dev
BuildRequires : pkgconfig(libsasl2)
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kimap-25.04.2
cd %{_builddir}/kimap-25.04.2
pushd ..
cp -a kimap-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749512928
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
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1749512928
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
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libkimap6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kimap.categories
/usr/share/qlogging-categories6/kimap.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KIMAP/KIMAP/Acl
/usr/include/KPim6/KIMAP/KIMAP/AclJobBase
/usr/include/KPim6/KIMAP/KIMAP/AppendJob
/usr/include/KPim6/KIMAP/KIMAP/CapabilitiesJob
/usr/include/KPim6/KIMAP/KIMAP/CloseJob
/usr/include/KPim6/KIMAP/KIMAP/CopyJob
/usr/include/KPim6/KIMAP/KIMAP/CreateJob
/usr/include/KPim6/KIMAP/KIMAP/DeleteAclJob
/usr/include/KPim6/KIMAP/KIMAP/DeleteJob
/usr/include/KPim6/KIMAP/KIMAP/EnableJob
/usr/include/KPim6/KIMAP/KIMAP/ExpungeJob
/usr/include/KPim6/KIMAP/KIMAP/FetchJob
/usr/include/KPim6/KIMAP/KIMAP/GetAclJob
/usr/include/KPim6/KIMAP/KIMAP/GetMetaDataJob
/usr/include/KPim6/KIMAP/KIMAP/GetQuotaJob
/usr/include/KPim6/KIMAP/KIMAP/GetQuotaRootJob
/usr/include/KPim6/KIMAP/KIMAP/IdJob
/usr/include/KPim6/KIMAP/KIMAP/IdleJob
/usr/include/KPim6/KIMAP/KIMAP/ImapSet
/usr/include/KPim6/KIMAP/KIMAP/Job
/usr/include/KPim6/KIMAP/KIMAP/ListJob
/usr/include/KPim6/KIMAP/KIMAP/ListRightsJob
/usr/include/KPim6/KIMAP/KIMAP/LoginJob
/usr/include/KPim6/KIMAP/KIMAP/LogoutJob
/usr/include/KPim6/KIMAP/KIMAP/MetaDataJobBase
/usr/include/KPim6/KIMAP/KIMAP/MoveJob
/usr/include/KPim6/KIMAP/KIMAP/MyRightsJob
/usr/include/KPim6/KIMAP/KIMAP/NamespaceJob
/usr/include/KPim6/KIMAP/KIMAP/QuotaJobBase
/usr/include/KPim6/KIMAP/KIMAP/RFCCodecs
/usr/include/KPim6/KIMAP/KIMAP/RenameJob
/usr/include/KPim6/KIMAP/KIMAP/SearchJob
/usr/include/KPim6/KIMAP/KIMAP/SelectJob
/usr/include/KPim6/KIMAP/KIMAP/Session
/usr/include/KPim6/KIMAP/KIMAP/SessionUiProxy
/usr/include/KPim6/KIMAP/KIMAP/SetAclJob
/usr/include/KPim6/KIMAP/KIMAP/SetMetaDataJob
/usr/include/KPim6/KIMAP/KIMAP/SetQuotaJob
/usr/include/KPim6/KIMAP/KIMAP/StatusJob
/usr/include/KPim6/KIMAP/KIMAP/StoreJob
/usr/include/KPim6/KIMAP/KIMAP/SubscribeJob
/usr/include/KPim6/KIMAP/KIMAP/UnsubscribeJob
/usr/include/KPim6/KIMAP/kimap/Acl
/usr/include/KPim6/KIMAP/kimap/AclJobBase
/usr/include/KPim6/KIMAP/kimap/AppendJob
/usr/include/KPim6/KIMAP/kimap/CapabilitiesJob
/usr/include/KPim6/KIMAP/kimap/CloseJob
/usr/include/KPim6/KIMAP/kimap/CopyJob
/usr/include/KPim6/KIMAP/kimap/CreateJob
/usr/include/KPim6/KIMAP/kimap/DeleteAclJob
/usr/include/KPim6/KIMAP/kimap/DeleteJob
/usr/include/KPim6/KIMAP/kimap/EnableJob
/usr/include/KPim6/KIMAP/kimap/ExpungeJob
/usr/include/KPim6/KIMAP/kimap/FetchJob
/usr/include/KPim6/KIMAP/kimap/GetAclJob
/usr/include/KPim6/KIMAP/kimap/GetMetaDataJob
/usr/include/KPim6/KIMAP/kimap/GetQuotaJob
/usr/include/KPim6/KIMAP/kimap/GetQuotaRootJob
/usr/include/KPim6/KIMAP/kimap/IdJob
/usr/include/KPim6/KIMAP/kimap/IdleJob
/usr/include/KPim6/KIMAP/kimap/ImapSet
/usr/include/KPim6/KIMAP/kimap/Job
/usr/include/KPim6/KIMAP/kimap/ListJob
/usr/include/KPim6/KIMAP/kimap/ListRightsJob
/usr/include/KPim6/KIMAP/kimap/LoginJob
/usr/include/KPim6/KIMAP/kimap/LogoutJob
/usr/include/KPim6/KIMAP/kimap/MetaDataJobBase
/usr/include/KPim6/KIMAP/kimap/MoveJob
/usr/include/KPim6/KIMAP/kimap/MyRightsJob
/usr/include/KPim6/KIMAP/kimap/NamespaceJob
/usr/include/KPim6/KIMAP/kimap/QuotaJobBase
/usr/include/KPim6/KIMAP/kimap/RFCCodecs
/usr/include/KPim6/KIMAP/kimap/RenameJob
/usr/include/KPim6/KIMAP/kimap/SearchJob
/usr/include/KPim6/KIMAP/kimap/SelectJob
/usr/include/KPim6/KIMAP/kimap/Session
/usr/include/KPim6/KIMAP/kimap/SessionUiProxy
/usr/include/KPim6/KIMAP/kimap/SetAclJob
/usr/include/KPim6/KIMAP/kimap/SetMetaDataJob
/usr/include/KPim6/KIMAP/kimap/SetQuotaJob
/usr/include/KPim6/KIMAP/kimap/StatusJob
/usr/include/KPim6/KIMAP/kimap/StoreJob
/usr/include/KPim6/KIMAP/kimap/SubscribeJob
/usr/include/KPim6/KIMAP/kimap/UnsubscribeJob
/usr/include/KPim6/KIMAP/kimap/acl.h
/usr/include/KPim6/KIMAP/kimap/acljobbase.h
/usr/include/KPim6/KIMAP/kimap/appendjob.h
/usr/include/KPim6/KIMAP/kimap/capabilitiesjob.h
/usr/include/KPim6/KIMAP/kimap/closejob.h
/usr/include/KPim6/KIMAP/kimap/copyjob.h
/usr/include/KPim6/KIMAP/kimap/createjob.h
/usr/include/KPim6/KIMAP/kimap/deleteacljob.h
/usr/include/KPim6/KIMAP/kimap/deletejob.h
/usr/include/KPim6/KIMAP/kimap/enablejob.h
/usr/include/KPim6/KIMAP/kimap/expungejob.h
/usr/include/KPim6/KIMAP/kimap/fetchjob.h
/usr/include/KPim6/KIMAP/kimap/getacljob.h
/usr/include/KPim6/KIMAP/kimap/getmetadatajob.h
/usr/include/KPim6/KIMAP/kimap/getquotajob.h
/usr/include/KPim6/KIMAP/kimap/getquotarootjob.h
/usr/include/KPim6/KIMAP/kimap/idjob.h
/usr/include/KPim6/KIMAP/kimap/idlejob.h
/usr/include/KPim6/KIMAP/kimap/imapset.h
/usr/include/KPim6/KIMAP/kimap/job.h
/usr/include/KPim6/KIMAP/kimap/kimap_export.h
/usr/include/KPim6/KIMAP/kimap/listjob.h
/usr/include/KPim6/KIMAP/kimap/listrightsjob.h
/usr/include/KPim6/KIMAP/kimap/loginjob.h
/usr/include/KPim6/KIMAP/kimap/logoutjob.h
/usr/include/KPim6/KIMAP/kimap/metadatajobbase.h
/usr/include/KPim6/KIMAP/kimap/movejob.h
/usr/include/KPim6/KIMAP/kimap/myrightsjob.h
/usr/include/KPim6/KIMAP/kimap/namespacejob.h
/usr/include/KPim6/KIMAP/kimap/quotajobbase.h
/usr/include/KPim6/KIMAP/kimap/renamejob.h
/usr/include/KPim6/KIMAP/kimap/rfccodecs.h
/usr/include/KPim6/KIMAP/kimap/searchjob.h
/usr/include/KPim6/KIMAP/kimap/selectjob.h
/usr/include/KPim6/KIMAP/kimap/session.h
/usr/include/KPim6/KIMAP/kimap/sessionuiproxy.h
/usr/include/KPim6/KIMAP/kimap/setacljob.h
/usr/include/KPim6/KIMAP/kimap/setmetadatajob.h
/usr/include/KPim6/KIMAP/kimap/setquotajob.h
/usr/include/KPim6/KIMAP/kimap/statusjob.h
/usr/include/KPim6/KIMAP/kimap/storejob.h
/usr/include/KPim6/KIMAP/kimap/subscribejob.h
/usr/include/KPim6/KIMAP/kimap/unsubscribejob.h
/usr/include/KPim6/KIMAP/kimap_version.h
/usr/include/KPim6/KIMAPTest/kimaptest/fakeserver.h
/usr/include/KPim6/KIMAPTest/kimaptest/mockjob.h
/usr/lib64/cmake/KPim6IMAP/KPim6IMAPConfig.cmake
/usr/lib64/cmake/KPim6IMAP/KPim6IMAPConfigVersion.cmake
/usr/lib64/cmake/KPim6IMAP/KPim6IMAPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6IMAP/KPim6IMAPTargets.cmake
/usr/lib64/libKPim6IMAP.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6IMAP.so.6.4.2
/usr/lib64/libKPim6IMAP.so.6
/usr/lib64/libKPim6IMAP.so.6.4.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kimap/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kimap/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kimap/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kimap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kimap/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libkimaptest6.a

%files locales -f libkimap6.lang
%defattr(-,root,root,-)

