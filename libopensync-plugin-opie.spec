Summary:	OpenSync Plugin for Opie
Summary(pl.UTF-8):	Wtyczka Opie do OpenSync
Name:		libopensync-plugin-opie
Version:	0.22
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	29b0fea90a4782f68e8017db32e3b6ea
URL:		http://www.opensync.org/
BuildRequires:	curl-devel
BuildRequires:	glib2-devel >= 1:2.10
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.10
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/{plugins,formats}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/opensync/plugins/opie_sync.so
%attr(755,root,root) %{_libdir}/opensync/formats/opie.so
%{_datadir}/opensync/defaults/opie-sync

# devel
#%{_includedir}/opensync-1.0/opensync/opie_sync.h
