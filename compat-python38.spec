Name:           compat-python38
Version:        3.8.1
Release:        30
License:        Python-2.0
Summary:        The Python Programming Language
Url:            http://www.python.org
Group:          devel/python
Source0:        https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz

BuildRequires:  bzip2
BuildRequires:  db
BuildRequires:  grep
BuildRequires:  bzip2-dev
BuildRequires:  xz-dev
BuildRequires:  gdbm-dev
BuildRequires:  readline-dev
BuildRequires:  openssl
BuildRequires:  openssl-dev
BuildRequires:  sqlite-autoconf
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  ncurses-dev
BuildRequires:  expat-dev
BuildRequires:  libffi-dev
BuildRequires:  procps-ng-bin
BuildRequires:  netbase
Requires: compat-python38-core
Requires: compat-python38-lib
Requires: usrbinpython

Patch1: 0001-Fix-python-path-for-linux.patch


%global __arch_install_post %{nil}

%description
The Python Programming Language.

%package lib
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python

%description lib
The Python Programming Language.

%package lib-avx2
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python
Requires:       compat-python38-lib

%description lib-avx2
The Python Programming Language.

%package core
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python



%description core
The Python Programming Language.

%package dev
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel
Requires:       compat-python38-lib
Requires:       compat-python38-core
Requires:       usrbinpython

%define python_configure_flags  --with-threads --with-pymalloc  --without-cxx-main --with-signal-module --enable-ipv6=yes  --libdir=/usr/lib  ac_cv_header_bluetooth_bluetooth_h=no  ac_cv_header_bluetooth_h=no  --with-system-ffi --with-system-expat --with-lto=8 --with-computed-gotos


%description dev
The Python Programming Language.

%package doc
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python

%description doc
The Python Programming Language.

%prep
%setup -q -n Python-%{version}

%patch1 -p1

%build
export LANG=C

# Build with PGO for perf improvement
export CFLAGS="$CFLAGS -O3"
%configure %python_configure_flags --enable-shared
make %{?_smp_mflags}

%install

%make_install
mv %{buildroot}/usr/lib/libpython*.so* %{buildroot}/usr/lib64/

%check
export LANG=C
#LD_LIBRARY_PATH=`pwd` ./python -Wd -E -tt  Lib/test/regrtest.py -v -x test_asyncio test_uuid test_subprocess || :


%files

%files lib
/usr/lib64/libpython3.8.so.1.0

%files lib-avx2

%files core
%exclude /usr/bin/2to3
%exclude /usr/bin/2to3-3.8
%exclude /usr/bin/idle3
%exclude /usr/bin/idle3.8
%exclude /usr/bin/pip3
%exclude /usr/bin/pip3.8
%exclude /usr/bin/pydoc3
/usr/bin/pydoc3.8
%exclude /usr/bin/python3
%exclude /usr/bin/python3-config
/usr/bin/python3.8
/usr/bin/python3.8-config
/usr/bin/python3.8
/usr/bin/python3.8-config
/usr/lib/python3.8/
%exclude /usr/lib/python3.8/site-packages/pip
%exclude /usr/lib/python3.8/distutils/command/*.exe


%files dev
%exclude /usr/include/python3.8/*.h
%exclude /usr/lib64/libpython3.so
%exclude /usr/lib64/libpython3.8.so
%exclude /usr/lib64/pkgconfig/python3.pc
%exclude /usr/lib64/pkgconfig/python-3.8.pc
%exclude /usr/lib64/pkgconfig/python-3.8.pc
   /usr/include/python3.8/cpython/abstract.h
   /usr/include/python3.8/cpython/dictobject.h
   /usr/include/python3.8/cpython/fileobject.h
   /usr/include/python3.8/cpython/initconfig.h
   /usr/include/python3.8/cpython/interpreteridobject.h
   /usr/include/python3.8/cpython/object.h
   /usr/include/python3.8/cpython/objimpl.h
   /usr/include/python3.8/cpython/pyerrors.h
   /usr/include/python3.8/cpython/pylifecycle.h
   /usr/include/python3.8/cpython/pymem.h
   /usr/include/python3.8/cpython/pystate.h
   /usr/include/python3.8/cpython/sysmodule.h
   /usr/include/python3.8/cpython/traceback.h
   /usr/include/python3.8/cpython/tupleobject.h
   /usr/include/python3.8/cpython/unicodeobject.h
   /usr/include/python3.8/internal/pycore_accu.h
   /usr/include/python3.8/internal/pycore_atomic.h
   /usr/include/python3.8/internal/pycore_ceval.h
   /usr/include/python3.8/internal/pycore_code.h
   /usr/include/python3.8/internal/pycore_condvar.h
   /usr/include/python3.8/internal/pycore_context.h
   /usr/include/python3.8/internal/pycore_fileutils.h
   /usr/include/python3.8/internal/pycore_getopt.h
   /usr/include/python3.8/internal/pycore_gil.h
   /usr/include/python3.8/internal/pycore_hamt.h
   /usr/include/python3.8/internal/pycore_initconfig.h
   /usr/include/python3.8/internal/pycore_object.h
   /usr/include/python3.8/internal/pycore_pathconfig.h
   /usr/include/python3.8/internal/pycore_pyerrors.h
   /usr/include/python3.8/internal/pycore_pyhash.h
   /usr/include/python3.8/internal/pycore_pylifecycle.h
   /usr/include/python3.8/internal/pycore_pymem.h
   /usr/include/python3.8/internal/pycore_pystate.h
   /usr/include/python3.8/internal/pycore_traceback.h
   /usr/include/python3.8/internal/pycore_tupleobject.h
   /usr/include/python3.8/internal/pycore_warnings.h
   /usr/lib64/pkgconfig/python-3.8-embed.pc
   /usr/lib64/pkgconfig/python3-embed.pc

%files doc
%exclude %{_mandir}/man1/*
