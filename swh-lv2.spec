%define debug_package	%{nil}

Summary:    SWH LV2 plugins converted from LADSPA
Name:       swh-lv2
Version:    1.0.16
Release:    1
License:    GPLv2+
Group:      Sound
URL:        http://plugin.org.uk/
#Source0:    http://plugin.org.uk/lv2/%{name}-%{version}.tar.gz
Source0:    https://github.com/swh/lv2/archive/refs/tags/v%{version}/lv2-%{version}.tar.gz
BuildRequires:  fftw3-devel
BuildRequires:  ladspa-devel
BuildRequires:  lv2-devel
BuildRequires:  xsltproc
Requires:   lv2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is an early experimental port of my LADSPA plugins to the LV2
specification, c.f. http://lv2plug.in/ . It's still quite early days, but most
things should work as well or not as they did in LADSPA.

%prep

%setup -q -n lv2-%{version}

%build

%make LDFLAGS="-lm"

%install
rm -rf %{buildroot}

make install-system \
    PREFIX=%{buildroot} \
    INSTALL_DIR=%{buildroot}%{_libdir}/lv2
chmod 644 %{buildroot}%{_libdir}/lv2/*/*.ttl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/lv2/*



%changelog
* Wed Apr 25 2012 Frank Kober <emuse@mandriva.org> 1.0.15-3
+ Revision: 793440
- rebuild adjusting BR and adding missing lm link

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0.15-2mdv2010.0
+ Revision: 445302
- rebuild

* Tue Nov 25 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.15-1mdv2009.1
+ Revision: 306687
- import swh-lv2


* Tue Nov 25 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.15-1mdv2009.0
- initial Mandriva package
