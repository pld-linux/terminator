Summary:	Store and run multiple GNOME terminals in one window
Name:		terminator
Version:	0.96
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://code.launchpad.net/terminator/trunk/%{version}/+download/%{name}_%{version}.tar.gz
# Source0-md5:	070e3878336b341c9e18339d89ba64fe
Patch0:		%{name}-fix-NewWindow-issue.patch
URL:		http://www.tenshu.net/terminator
BuildRequires:	desktop-file-utils
BuildRequires:	rpm-pythonprov
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.596
Requires(post,postun):	hicolor-icon-theme
Requires:	GConf2
Requires:	desktop-file-utils
Requires:	gtk+2
Requires:	python-gnome-bonobo
Requires:	python-gnome-bonobo-ui
Requires:	python-gnome-gconf
Requires:	python-modules
Requires:	vte
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multiple GNOME terminals in one window. This is a project to produce
an efficient way of filling a large area of screen space with
terminals. This is done by splitting the window into a resizeable grid
of terminals. As such, you can produce a very flexible arrangements of
terminals for different tasks.

%prep
%setup -q
%patch0

%{__sed} -i '/#! \?\/usr.*/d' terminatorlib/*.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT/%{_datadir}/locale/{jv,ru_RU,tyv}
%{__rm} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/icon-theme.cache

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README COPYING ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/%{name}*.png
%{_iconsdir}/hicolor/*/*/%{name}*.svg
%{_iconsdir}/hicolor/16x16/status/terminal-bell.png
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}_config.*
