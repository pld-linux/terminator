Summary:	Store and run multiple GNOME terminals in one window
Name:		terminator
Version:	2.1.4
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	https://github.com/gnome-terminator/terminator/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	43205f75db40d27f74cd8fac81b4b887
Patch0:		%{name}-fix-NewWindow-issue.patch
URL:		https://github.com/gnome-terminator/terminator
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.596
Requires(post,postun):	hicolor-icon-theme
Requires:	desktop-file-utils
Requires:	gtk+3
Requires:	libnotify
Requires:	keybinder3
Requires:	python3-configobj
Requires:	python3-modules
Requires:	python3-psutil
Requires:	python3-pygobject3
Requires:	vte2.90
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
%patch -P 0

%{__sed} -i '/#! \?\/usr.*/d' terminatorlib/*.py

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{jv,ru_RU,su,tyv}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/remotinator
%{py3_sitescriptdir}/terminatorlib
%{py3_sitescriptdir}/terminator-%{version}-py3*.egg-info
%{_datadir}/terminator
%{_datadir}/metainfo/terminator.metainfo.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/%{name}*.png
%{_iconsdir}/hicolor/*/*/%{name}*.svg
%{_iconsdir}/hicolor/16x16/status/terminal-bell.png
%{_iconsdir}/HighContrast/*/*/%{name}*.png
%{_iconsdir}/HighContrast/*/*/%{name}*.svg
%{_iconsdir}/HighContrast/16x16/status/terminal-bell.png
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}_config.*
