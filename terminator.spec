Summary:	Store and run multiple GNOME terminals in one window
Name:		terminator
Version:	0.97
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://code.launchpad.net/terminator/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	2b32b59c0a5ed2bee45cc57cf861f4d8
Patch0:		%{name}-fix-NewWindow-issue.patch
URL:		http://gnometerminator.blogspot.com/
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.596
Requires(post,postun):	hicolor-icon-theme
Requires:	GConf2
Requires:	desktop-file-utils
Requires:	gtk+2
Requires:	python-gnome-bonobo
Requires:	python-gnome-bonobo-ui
Requires:	python-gnome-gconf
Requires:	python-keybinder
Requires:	python-modules
Requires:	python-vte0
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

%{__rm} -r $RPM_BUILD_ROOT/%{_localedir}/{jv,ru_RU,tyv}
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
