Summary:	Objective Open H.323 libraries
Summary(pl.UTF-8):	Biblioteki Objective Open H.323
Name:		ooh323c
Version:	0.9.3
Release:	2
License:	GPL v2 with FLOSS exception
Group:		Libraries
Source0:	http://downloads.sourceforge.net/ooh323c/%{name}-%{version}.tar.gz
# Source0-md5:	d557140e31bb592ec8fc9b6eb92908db
Patch0:		%{name}-no-common.patch
URL:		https://sourceforge.net/projects/ooh323c
BuildRequires:	cmake >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Objective Open H.323 stack.

%description -l pl.UTF-8
Stos Objective Open H.323.

%package devel
Summary:	Header files for ooh323c libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek ooh323c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ooh323c libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek ooh323c.

%package static
Summary:	Static ooh323c libraries
Summary(pl.UTF-8):	Statyczne biblioteki ooh323c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ooh323c libraries.

%description static -l pl.UTF-8
Statyczne biblioteki ooh323c.

%package apidocs
Summary:	API documentation for ooh323c libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek ooh323c
Group:		Documentation
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
API documentation for ooh323c libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek ooh323c.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/ooh323c}

cp -pr lib/lib* $RPM_BUILD_ROOT%{_libdir}
cp -p src/{dlist.h,eventHandler.h,ooCalls.h,ooCapability.h,ooCommon.h,ooLogChan.h,ooSocket.h,ooasn1.h,ooh323.h,ooq931.h,ootrace.h,ootypes.h,printHandler.h} \
	$RPM_BUILD_ROOT%{_includedir}/ooh323c
cp -p src/h323/H235-SECURITY-MESSAGES.h $RPM_BUILD_ROOT%{_includedir}/ooh323c
cp -p src/h323_v6/{H323-MESSAGES.h,MULTIMEDIA-SYSTEM-CONTROL.h} $RPM_BUILD_ROOT%{_includedir}/ooh323c

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libooh323c.so
%attr(755,root,root) %{_libdir}/liboomedia.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/ooh323c

%files static
%defattr(644,root,root,755)
%{_libdir}/libooh323c.a
%{_libdir}/liboomedia.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/{h323stk,*.shtml,*.css,*.pdf}
