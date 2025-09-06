Summary:	OpenSync Plugin for Opie
Summary(pl.UTF-8):	Wtyczka Opie do OpenSync
Name:		libopensync-plugin-opie
Version:	0.38
Release:	1
License:	GPL v2
Group:		Libraries
# originally http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw, dead now
# taken from http://ftp.iij.ad.jp/pub/linux/momonga/6/Everything/SOURCES/libopensync-plugin-opie-0.38.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	5af4a3afd3f497edd682f1c88dfebf48
Patch0:		%{name}-libopensync0.39.patch
# domain dead
#URL:		http://www.opensync.org/
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	glib2-devel >= 1:2.10
BuildRequires:	libopensync-devel >= 0.39
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	glib2 >= 1:2.10
Requires:	libopensync >= 0.39
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This OpenSync plugin is intended to allow synchronisation with the
Opie handheld environment <http://opie.handhelds.org/>. In theory it
should also support some versions of Qtopia as found on the Sharp
Zaurus, but no testing of this has been done.

%description -l pl.UTF-8
Celem tej wtyczki do OpenSync jest umożliwienie synchronizacji ze
środowiskiem PDA Opie <http://opie.handhelds.org/>. Teoretycznie
powinna obsługiwać także niektóre wersji Qtopii używanej w
urządzeniach Sharp Zaurus, ale nie było to testowane.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libopensync1/formats/opie.so
%attr(755,root,root) %{_libdir}/libopensync1/plugins/opie-sync.so
%{_datadir}/libopensync1/defaults/opie-sync
