Summary:	OpenSync Plugin for Opie
Name:		libopensync-plugin-opie
Version:	0.22
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	29b0fea90a4782f68e8017db32e3b6ea
URL:		http://www.opensync.org/
BuildRequires:	libopensync-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This OpenSync plugin is intended to allow synchronisation with the Opie
handheld environment <http://opie.handhelds.org>. In theory it should also
support some versions of Qtopia as found on the Sharp Zaurus, but no testing of
this has been done.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
%attr(755,root,root) %{_libdir}/opensync/formats/*.so
%{_libdir}/opensync/formats/*.la
%{_datadir}/opensync/defaults/*
