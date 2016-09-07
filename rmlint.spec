%define debug_package %nil
%bcond_with python3

Summary:        Extremely fast tool to remove duplicates
Name:           rmlint
Version:        2.4.4
Release:        1
License:        GPLv3
Group:          Monitoring
Url:            http://rmlint.rtfd.org/
Source0:	https://github.com/sahib/rmlint/archive/v%{version}.tar.gz

BuildRequires:  scons
BuildRequires:  json-glib-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  elfutils-devel
BuildRequires:  python-sphinx
%if %{with python3}
BuildRequires:  python-devel
Requires:	python-shredder
%endif

%description
rmlint finds space waste and other broken things on your filesystem
and offers to remove it.

%if %{with python3}
%package -n python-shredder
Summary: Runtime module for %{name}
Group:	Development/Python

%description -n python-shredder
rmlint finds space waste and other broken things on your filesystem
and offers to remove it.
%endif

%prep
%setup -q

%build
%setup_compile_flags
%scons CC="%{__cc}" CFLAGS="%{optflags}" DEBUG=1

%install
%scons_install LIBDIR="%{_libdir}" --prefix="%{buildroot}/%{_prefix}"
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%if %{with python3}
%{_datadir}/applications/shredder.desktop
%{_datadir}/glib-2.0/schemas/*.compiled
%{_datadir}/glib-2.0/schemas/org.gnome.Shredder.gschema.xml
%{_iconsdir}/hicolor/scalable/apps/shredder.svg
%endif

%if %{with python3}
%files -n python-shredder
%{python_sitelib}/shredder
%{python_sitelib}/Shredder*
%endif
