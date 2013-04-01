Summary:	An interface library to access tags for identifying languages
Summary(pl.UTF-8):	Biblioteka interfejsu dostępu do znaczników identyfikujących języki
Name:		liblangtag
Version:	0.4.0
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://bitbucket.org/tagoh/liblangtag/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	54e578c91b1b68e69c72be22adcb2195
Patch0:		0001-Fix-build-issues-with-MSVC.patch
Patch1:		%{name}-Werror.patch
URL:		http://tagoh.bitbucket.org/liblangtag/
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liblangtag is an interface library to access tags for identifying
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

%description -l pl.UTF-8
liblangtag to biblioteka interfejsu dostępu do znaczników
identyfikujących języki.

Możliwości:
- baza danych rejestru podznaczników obsługująca:
  - język
  - extlang
  - pismo
  - region
  - wariant
  - rozszerzenie
  - dziedziczenie
  - nadmiarowość
- obsługa znaczników języków:
  - analiza
  - dopasowywanie
  - sprowadzanie do postaci kanonicznej

%package devel
Summary:	Development files for liblangtag
Summary(pl.UTF-8):	Pliki programistyczne biblioteki liblangtag
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use liblangtag.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę liblangtag.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-introspection \
	--disable-silent-rules \
	--enable-shared \
	--disable-static \

%{__make} \
	LD_LIBRARY_PATH=`pwd`/liblangtag/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/liblangtag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblangtag.so.1
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/liblangtag-ext-ldml-t.so
%attr(755,root,root) %{_libdir}/%{name}/liblangtag-ext-ldml-u.so
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc docs/html/*
%attr(755,root,root)  %{_libdir}/liblangtag.so
%{_includedir}/liblangtag
%{_pkgconfigdir}/liblangtag.pc
