%define	name	gperiodic
%define	version 2.0.10
%define	release	%mkrel 1
%define summary A graphical application for browsing the periodic table
%define group	Sciences/Chemistry

Name:		%{name} 
Summary:	%{summary}
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://koti.welho.com/jfrantz/software/gperiodic.html
Group:		%{group}
License:	GPL
BuildRequires:	gtk2-devel ImageMagick
#BuildRequires:	

%description
Gperiodic displays a periodic table of the elements, allowing you to
browse through the elements, and view detailed information about each
element.

%prep
%setup -q

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

%post
%{update_menus}
%{update_icon_cache} hicolor

%postun
%{clean_menus}
%{clean_icon_cache} hicolor

%clean 
rm -rf $RPM_BUILD_ROOT 

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
