Summary:	Web Site CReating and Editing EnvironMent
Name:		screem
Version:	0.3.0
Release:	4
License:	GPL
Group:		X11/Applications/Editors
Group(de):	X11/Applikationen/Editors
Group(pl):	X11/Aplikacje/Edytory
Group(pt):	X11/Aplicações/Editores
Source0:	ftp://download.sourceforge.net/pub/sourceforge/screem/%{name}-%{version}.tar.gz
URL:		http://www.screem.org/
BuildRequires:	gdk-pixbuf-devel >= 0.7
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	gnome-print-devel >= 0.24
BuildRequires:	guile-devel
BuildRequires:	libxml-devel >= 1.8.7
BuildRequires:	libglade-devel >= 0.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
SCREEM (Site CReating and Editing EnvironMent) is an integrated
development environment for the creation and maintainance of websites
and pages.

%prep
%setup -q

%build
gettextize --copy --force
%configure \
	--enable-static=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Office/Editors

gzip -9nf ChangeLog NEWS README TODO FAQ BUGS DEPENDS

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/screem
%dir %{_libdir}/screem/plugins
%attr(755,root,root) %{_libdir}/screem/plugins/*
%{_datadir}/screem
%{_pixmapsdir}/*
%{_datadir}/mime-info/screem.keys
%{_datadir}/mime-info/screem.mime
%{_applnkdir}/Office/Editors/screem.desktop
