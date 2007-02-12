Summary:	Web Site CReating and Editing EnvironMent
Summary(pl.UTF-8):   Środowisko do tworzenia i edycji serwisów WWW
Name:		screem
Version:	0.16.1
Release:	3
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/screem/%{name}-%{version}.tar.gz
# Source0-md5:	88bfc0afadb905ddbed9bdfbc869602a
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-deprecations.patch
URL:		http://www.screem.org/
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.22
BuildRequires:	enchant-devel >= 1.1.6
BuildRequires:	gnome-menus-devel >= 2.10.0
BuildRequires:	gnome-vfs2-devel >= 2.8.3
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	gtksourceview-devel >= 1.2.0
BuildRequires:	intltool >= 0.29
BuildRequires:	libbonoboui-devel >= 2.4.0
BuildRequires:	libcroco-devel >= 0.6.0
BuildRequires:	libglade2-devel >= 2.3.0
BuildRequires:	libgnome-devel >= 2.2.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libgtkhtml-devel >= 2.4.3
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
BuildRequires:	startup-notification-devel >= 0.5
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCREEM (Site CReating and Editing EnvironMent) is an integrated
development environment for the creation and maintainance of websites
and pages.

%description -l pl.UTF-8
SCREEM (Site CReating and Editing EnvironMent) jest zintegrowanym
środowiskiem do tworzenia i prowadzenia serwisów i stron WWW.

%package devel
Summary:	SCREEM header files
Summary(pl.UTF-8):   Pliki nagłówkowe SCREEM
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-vfs2-devel >= 2.8.3
Requires:	gtk+2-devel >= 2:2.6.4
Requires:	gtksourceview-devel >= 1.2.0
Requires:	libxml2-devel >= 2.4.3

%description devel
SCREEM header files for plugin development.

%description devel -l pl.UTF-8
Pliki nagłówkowe SCREEM do tworzenia wtyczek.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-dbus \
	--enable-enchant \
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
rm -r $RPM_BUILD_ROOT%{_datadir}/application-registry

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install screem.schemas
%scrollkeeper_update_post
%update_desktop_database_post
umask 022
update-mime-database %{_datadir}/mime ||:

%preun
%gconf_schema_uninstall screem.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
if [ $1 = 0 ]; then
	umask 022
	update-mime-database %{_datadir}/mime
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README BUGS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/screem
%dir %{_libdir}/screem/plugins
%attr(755,root,root) %{_libdir}/screem/plugins/*.so
%{_datadir}/screem
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/screem.schemas
%{_datadir}/mime/packages/*
%{_desktopdir}/screem.desktop
%{_omf_dest_dir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
