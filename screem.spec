Summary:	Web Site CReating and Editing EnvironMent
Summary(pl):	Środowisko do tworzenia i edycji serwisów WWW
Name:		screem
Version:	0.12.1
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4d1f50deee2888f0ac094cb3df61f1ad
Patch0:		%{name}-desktop.patch
URL:		http://www.screem.org/
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.22
BuildRequires:	gdk-pixbuf-devel >= 2.2.0
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel >= 2.8.0
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	gtksourceview-devel
BuildRequires:	intltool >= 0.18
BuildRequires:	libbonobo-devel
BuildRequires:	libbonoboui-devel >= 2.4.0
BuildRequires:	libglade2-devel >= 2.3.0
BuildRequires:	libgnome-devel >= 2.2.0
BuildRequires:	libgnomeprint-devel >= 2.2.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libgtkhtml-devel >= 2.4.3
BuildRequires:	libxml2-devel >= 2.4.3
BuildRequires:	perl-XML-Parser
BuildRequires:	scrollkeeper
Requires(post):	GConf2
Requires(post):	/usr/bin/scrollkeeper-update
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCREEM (Site CReating and Editing EnvironMent) is an integrated
development environment for the creation and maintainance of websites
and pages.

%description -l pl
SCREEM (Site CReating and Editing EnvironMent) jest zintegrowanym
środowiskiem do tworzenia i prowadzenia serwisów i stron WWW.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%configure \
	--enable-dbus \
	--disable-update-mime \
	--disable-update-desktop \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

#remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/usr/bin/scrollkeeper-update
%gconf_schema_install
update-mime-database %{_datadir}/mime
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
/usr/bin/scrollkeeper-update
update-mime-database %{_datadir}/mime
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README BUGS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/screem
%dir %{_libdir}/screem/plugins
%attr(755,root,root) %{_libdir}/screem/plugins/*.so
%{_datadir}/screem
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/application-registry/screem.applications
%{_datadir}/mime-info/screem.*
%{_datadir}/mime/packages/*
%{_desktopdir}/screem.desktop
%{_omf_dest_dir}/%{name}
