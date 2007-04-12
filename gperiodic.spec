%define	name	gperiodic
%define	version 2.0.8
%define	release	%mkrel 3
%define summary A graphical application for browsing the periodic table
%define group	Sciences/Chemistry

Name:		%{name} 
Summary:	%{summary}
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://koti.welho.com/jfrantz/software/gperiodic.html
Group:		%{group}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
cd po/; make enable_nls=1;%makeinstall enable_nls=1; cd ..
install -m755 gperiodic -D $RPM_BUILD_ROOT%{_bindir}/gperiodic

# Icons
convert gperiodic-crystal.png -resize 32x32 gperiodic-crystal-32.png
convert gperiodic-crystal.png -resize 16x16 gperiodic-crystal-16.png
convert gperiodic.png -resize 32x32 gperiodic-32.png
convert gperiodic.png -resize 16x16 gperiodic-16.png
install -m644 ./gperiodic-crystal.png -D $RPM_BUILD_ROOT%{_liconsdir}/gperiodic-crystal.png
install -m644 ./gperiodic-crystal-16.png -D $RPM_BUILD_ROOT%{_miconsdir}/gperiodic-crystal.png
install -m644 ./gperiodic-crystal-32.png -D $RPM_BUILD_ROOT%{_iconsdir}/gperiodic-crystal.png
install -m644 ./gperiodic.png -D $RPM_BUILD_ROOT%{_iconsdir}/gperiodic.png
install -m644 ./gperiodic-16.png -D $RPM_BUILD_ROOT%{_miconsdir}/gperiodic.png
install -m644 ./gperiodic-32.png -D $RPM_BUILD_ROOT%{_iconsdir}/gperiodic.png


mkdir -p $RPM_BUILD_ROOT%{_menudir}/
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/gperiodic" \
                icon="gperiodic-crystal.png" \
                needs="x11" \
                section="More Applications/Sciences/Chemistry" \
                title="Gperiodic" \
                longtitle="%{summary}"
EOF
%find_lang %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%clean 
rm -rf $RPM_BUILD_ROOT 

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/gperiodic
%{_iconsdir}/*
%{_miconsdir}/*
%{_liconsdir}/*
%{_menudir}/%{name}


