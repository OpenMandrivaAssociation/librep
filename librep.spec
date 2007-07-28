%define major 9
%define libname %mklibname rep %major

Name:		librep
Summary:	An embeddable LISP environment
Version:	0.17
Release:	%mkrel 7
License:	GPL
Group:		System/Libraries
BuildRequires:	gmp-devel gdbm-devel gpm-devel ncurses-devel readline-devel texinfo
BuildRequires:  automake1.8
URL:		http://librep.sourceforge.net/
Source0:	http://ftp.gnome.org/stable/sources/librep/%{name}-%{version}.tar.bz2
Patch0:		librep-0.17-fix-underquoted-calls.patch.bz2
Requires(post): info-install
Requires(preun): info-install
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

%package -n	%{libname}-devel
Summary:	Librep include files and link libraries
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}

%description -n	%{libname}-devel
Link libraries and C header files for librep development.


%prep
%setup -q
%patch0 -p1 -b .underquoted
aclocal
autoconf||autoconf

%build
%configure2_5x --with-readline

%make host_type=%{_target_platform}

%install
rm -rf %{buildroot}
%makeinstall_std host_type=%{_target_platform}
%multiarch_binaries %buildroot%_bindir/rep-config

%post -n %{libname} -p /sbin/ldconfig

%post
%_install_info librep.info


%preun
%_remove_install_info librep.info

%postun -n %{libname}  -p /sbin/ldconfig


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
%{_libdir}/librep.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_bindir}/rep-config
%multiarch %{multiarch_bindir}/rep-config
%{_bindir}/rep-xgettext
%{_bindir}/repdoc
%{_libdir}/librep.so
%{_libdir}/librep.la
%{_includedir}/*
%{_libexecdir}/rep/%{_target_platform}
%{_datadir}/aclocal/rep.m4
