%define major 9
%define libname %mklibname rep %major
%define libnamedev %mklibname -d rep

Name:		librep
Summary:	An embeddable LISP environment
Version:	0.90.0
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Libraries
BuildRequires:	gmp-devel gdbm-devel gpm-devel ncurses-devel readline-devel texinfo
URL:		http://librep.sourceforge.net/
Source0:	http://downloads.sourceforge.net/librep/%{name}-%{version}.tar.bz2
Patch0:		librep-0.90.0-fix-build.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
This is a lightweight LISP environment for UNIX. It contains a LISP 
interpreter, byte-code compiler and virtual machine. Applications may use the 
LISP interpreter as an extension language, or it may be used for standalone 
scripts.

Originally inspired by Emacs Lisp, the language dialect combines many of the 
elisp features while trying to remove some of the main deficiencies, with 
features from Common Lisp and Scheme.

%package -n	%{libname}
Summary:	Libraries used by librep
Group:		System/Libraries

%description -n	%{libname}
Libraries used by librep

%package -n	%{libnamedev}
Summary:	Librep include files and link libraries
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%mklibname -d %name 9
Provides:	%{name}-devel = %{version}

%description -n	%{libnamedev}
Link libraries and C header files for librep development.


%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --with-readline
%make

%install
rm -rf %{buildroot}
%makeinstall_std host_type=%{_target_platform}
%multiarch_binaries %buildroot%_bindir/rep-config
rm -f %buildroot%{_libdir}/librep.a

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%post
%_install_info librep.info

%preun
%_remove_install_info librep.info

%if %mdkversion < 200900
%postun -n %{libname}  -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_bindir}/rep
%{_bindir}/rep-remote
%{_datadir}/rep
%dir %{_libexecdir}/rep
%{_libexecdir}/rep/%{version}
%{_infodir}/librep*
%{_datadir}/emacs/site-lisp/*.el

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/librep.so.9*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_bindir}/rep-config
%multiarch %{multiarch_bindir}/rep-config
%{_bindir}/rep-xgettext
%{_bindir}/repdoc
%{_libdir}/librep.so
%{_libdir}/librep.la
%{_includedir}/*
%_libdir/pkgconfig/librep.pc
%{_libexecdir}/rep/%{_target_platform}
