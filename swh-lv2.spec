Summary:	SWH LV2 plugins for LADSPA
Name:		swh-lv2
Version:	1.0.15
Release:	%mkrel 2
License:	GPLv2+
Group:		Sound
URL:		http://plugin.org.uk/
Source0:	http://plugin.org.uk/lv2/%{name}-%{version}.tar.gz
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	libxslt-proc
Requires:	ladspa
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is an early experimental port of my LADSPA plugins to the LV2
specification, c.f. http://lv2plug.in/ . It's still quite early days, but most
things should work as well or not as they did in LADSPA.

%prep

%setup -q

%build
%make CFLAGS="%{optflags} -fPIC"

%install
rm -rf %{buildroot}

make install-system \
    PREFIX=%{buildroot} \
    INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/lv2/*

