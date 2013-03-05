%define _disable_ld_no_undefined 1

%define major	16
%define libname %mklibname rep %major
%define devname %mklibname -d rep

%define _requires_exceptions /usr/bin/rep

Summary:	An embeddable LISP environment
Name:		librep
Version:	0.92.3
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://librep.sourceforge.net/
Source0:	http://download.tuxfamily.org/librep/%{name}-%{version}.tar.xz
Source1:	http://download.tuxfamily.org/librep/%{name}-%{version}.tar.xz.sha1

BuildRequires:	texinfo
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
BuildRequires:	gpm-devel
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(ncurses)


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

%package -n	%{devname}
Summary:	Librep include files and link libraries
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n	%{devname}
Link libraries and C header files for librep development.


%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--with-readline
%make

%install
%makeinstall_std host_type=%{_target_platform}

%files
%doc ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/rep
%{_bindir}/rep-remote
%{_libexecdir}/rep/
%{_infodir}/librep*
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/rep
%_mandir/man1/rep-remote.1*
%_mandir/man1/rep.1*

%files -n %{libname}
%{_libdir}/librep.so.%{major}*

%files -n %{devname}
%{_bindir}/rep-xgettext
%{_bindir}/repdoc
%_mandir/man1/rep-xgettext.1*
%_mandir/man1/repdoc.1*
%{_libdir}/librep.so
%{_includedir}/*
%_libdir/pkgconfig/librep.pc

