Summary:	An interface library to access tags for identifying languages
Name:		liblangtag
Version:	0.4.0
Release:	1
License:	LGPLv3+
Group:		Libraries
URL:		http://tagoh.bitbucket.org/liblangtag/
Source0:	https://bitbucket.org/tagoh/liblangtag/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	54e578c91b1b68e69c72be22adcb2195
Patch0:		0001-Fix-build-issues-with-MSVC.patch
Patch1:		%{name}-Werror.patch
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} is an interface library to access tags for identifying
languages.

Features:
- several subtag registry database supports:
  - language
  - extlang
  - script
  - region
  - variant
  - extension
  - grandfathered
  - redundant
- handling of the language tags
  - parser
  - matching
  - canonicalizing

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-static \
	--enable-shared \
	--disable-introspection \

%{__make} V=1 \
	LD_LIBRARY_PATH=`pwd`/liblangtag/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la $RPM_BUILD_ROOT/%{_libdir}/%{name}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.1
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/liblangtag-ext-ldml-t.so
%attr(755,root,root) %{_libdir}/%{name}/liblangtag-ext-ldml-u.so
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc docs/html/*
%attr(755,root,root)  %{_libdir}/%{name}.so
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc
