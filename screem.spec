%define	ver	0.2.10
%define	rel	1
%define	prefix	/usr

Summary: Web Site CReating and Editing EnvironMent
Name:	screem
Version:	%ver
Release:	%rel
Copyright:	GPL
Group:	Applications/
Source:	http://www.screem.org/src/screem-%{ver}.tar.gz
Url:	http://www.screem.org
BuildRoot:	/var/tmp/screem-%{PACKAGE_VERSION}-root
Obsoletes:	screem
Docdir:	%{prefix}/doc

Requires:	gnome-libs >= 1.2.0
Requires:	libxml >= 1.8.7
Requires:	libglade >= 0.12
Requires:	gdk-pixbuf >= 0.7

%description
SCREEM (Site CReating and Editing EnvironMent) is an integrated development
environment for the creation and maintainance of websites and pages.

%prep
%setup

%build
./configure --prefix=%prefix --enable-static=no --with-gnome=$RPM_BUILD_ROOT%{prefix}
make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc docs AUTHORS ChangeLog NEWS README COPYING TODO FAQ BUGS DEPENDS

%{prefix}/bin/*
%{prefix}/lib/screem/*
%{prefix}/share/screem/*
%{prefix}/share/pixmaps/screem*
%{prefix}/share/mime-info/screem.keys
%{prefix}/share/mime-info/screem.mime
%{prefix}/share/gnome/apps/Development/screem.desktop
%{prefix}/share/mc/templates/screem.desktop
