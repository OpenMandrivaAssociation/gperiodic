%define	name	gperiodic
%define	version 2.0.10
%define release	6
%define summary A graphical application for browsing the periodic table
%define group	Sciences/Chemistry

Name:		%{name} 
Summary:	%{summary}
Version:	%{version} 
Release:	%{release} 
Source0:	http://www.frantz.fi/software/%{name}-%{version}.tar.bz2
URL:		https://www.frantz.fi/software/gperiodic.php
Group:		%{group}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	gtk2-devel imagemagick
#BuildRequires:	

%description
Gperiodic displays a periodic table of the elements, allowing you to
browse through the elements, and view detailed information about each
element.

%prep
%setup -q
sed -i -e "s|-DGTK_DISABLE_DEPRECATED|%{optflags} %{ldflags}|" Makefile

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# Icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/16x16/apps/
convert -geometry 16x16 gperiodic.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}/hicolor/32x32/apps/
convert -geometry 32x32 gperiodic.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}/hicolor/48x48/apps/
convert -geometry 48x48 gperiodic.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache} hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache} hicolor
%endif

%clean 
rm -rf $RPM_BUILD_ROOT 

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.10-5mdv2011.0
+ Revision: 610974
- rebuild

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 2.0.10-4mdv2010.1
+ Revision: 506987
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 19 2007 Funda Wang <fwang@mandriva.org> 2.0.10-1mdv2008.0
+ Revision: 53609
- Use standard install method
- use fdo icon theme
- New version


* Mon Jan 15 2007 Lenny Cartier <lenny@mandriva.com> 2.0.8-3mdv2007.0
+ Revision: 109225
- Buildrequires
- Rebuild
- Import gperiodic

