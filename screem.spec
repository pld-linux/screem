Summary:	Web Site CReating and Editing EnvironMent
Summary(pl):	¦rodowisko do tworzenia i edycji serwisów WWW
Name:		screem
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Editors
# Source0-md5:	ee46df5d1ddc673c97b37b50145f510f
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.screem.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:  GConf2-devel
BuildRequires:  intltool >= 0.18
BuildRequires:  glib2-devel >= 2.2.0
BuildRequires:  libgnome-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libxml2-devel >= 2.4.3
BuildRequires:  libglade2-devel >= 1.99.2
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gtk+2-devel >= 2.2.0
BuildRequires:  libbonobo-devel
BuildRequires:  libbonoboui-devel
BuildRequires:  libgtkhtml-devel
BuildRequires:	libgnomeprint-devel >= 2.2.0
BuildRequires:  libgnomeprintui-devel >= 2.2.0
BuildRequires:  scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
SCREEM (Site CReating and Editing EnvironMent) is an integrated
development environment for the creation and maintainance of websites
and pages.

%description -l pl
SCREEM (Site CReating and Editing EnvironMent) jest zingtegrowanym
¶rodowiskiem do tworzenia i prowadzenia serwisów i stron WWW.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

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
%{_datadir}/mime-info/screem.mime
%{_desktopdir}/screem.desktop
%{_omf_dest_dir}/%{name}
