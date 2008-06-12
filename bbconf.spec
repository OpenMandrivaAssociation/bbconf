%define name		bbconf
%define version		1.10
%define release		%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://bbconf.sourceforge.net/
Source:		http://bbconf.sourceforge.net/code/%{name}-%{version}.tar.bz2
Source1:	%{name}-16x16.png.bz2
Source2:	%{name}-32x32.png.bz2
Source3:	%{name}-48x48.png.bz2
Group:		Graphical desktop/Other
License:	GPL
BuildRequires:	qt3-devel
BuildRequires:	X11-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
#Obsoletes:	bbkeysconf
BuildRoot:	%{_tmppath}/%{name}-%{version}
Summary:	Bbconf

%description
Bbconf is a complete GUI blackbox configuration tool.
It uses plugins to allow other developers to easily develop plugins 
to run inside bbconf to allow every aspect of blackbox and its 
companion programs to be configured easily in a single application.  
Bbconf comes with 4 plugins, allowing configuration of blackbox's 
keybindings, blackbox's menus, and blackbox's style files/themes.

%prep

%setup -q -n %{name}-%{version}
./configure 	--prefix=%_prefix \
		--exec-prefix=%_prefix \
		--bindir=%_bindir \
		--datadir=%_datadir \
		--libdir=%_libdir \
		--libexecdir=%_libdir \
		--mandir=%_mandir \


%build
%make

%install
mkdir -p $RPM_BUILD_ROOT
make install-strip DESTDIR=$RPM_BUILD_ROOT

# rm unpackaged files.
rm $RPM_BUILD_ROOT/usr/doc/bbconf/*

# Menu
  
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Bbconf
Comment=Bbconf is a complete GUI config tool for blackbox
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-System-Configuration-Other;Settings;
EOF

#icon
install -d $RPM_BUILD_ROOT/%{_iconsdir}
install -d $RPM_BUILD_ROOT/%{_miconsdir}
install -d $RPM_BUILD_ROOT/%{_liconsdir}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png
 
%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.html ChangeLog AUTHORS TODO COPYING
%attr(755,root,root) 
%_bindir/*
%_libdir/%name
%_mandir/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
%_iconsdir/%{name}.png
%_liconsdir/%{name}.png
%_miconsdir/%{name}.png
  
