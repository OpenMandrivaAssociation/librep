%define major 16
%define libname %mklibname rep %major
%define libnamedev %mklibname -d rep

%define _requires_exceptions /usr/bin/rep
Name:		librep
Summary:	An embeddable LISP environment
Version:	0.92.2
Release:	1
License:	GPLv2+
Group:		System/Libraries
BuildRequires:	gmp-devel gdbm-devel gpm-devel ncurses-devel readline-devel texinfo
BuildRequires: ffi5-devel
URL:		http://librep.sourceforge.net/
Source0:	http://download.tuxfamily.org/librep/%{name}-%{version}.tar.xz


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
%apply_patches

%build
%configure2_5x --with-readline
%make

%install
%makeinstall_std host_type=%{_target_platform}
rm -f %buildroot%{_libdir}/librep.*a


%post
%_install_info librep.info

%preun
%_remove_install_info librep.info


%files
%doc ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/rep
%{_bindir}/rep-remote
%{_datadir}/rep
%_mandir/man1/rep-remote.1*
%_mandir/man1/rep.1*
%{_libexecdir}/rep/
%{_infodir}/librep*
%{_datadir}/emacs/site-lisp/*.el

%files -n %{libname}
%{_libdir}/librep.so.%{major}*

%files -n %{libnamedev}
%{_bindir}/rep-xgettext
%{_bindir}/repdoc
%_mandir/man1/rep-xgettext.1*
%_mandir/man1/repdoc.1*
%{_libdir}/librep.so
%{_includedir}/*
%_libdir/pkgconfig/librep.pc


%changelog
* Tue Mar 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.92.2-1
+ Revision: 787890
- version update 0.92.2

* Fri Jan 06 2012 Götz Waschk <waschk@mandriva.org> 0.92.1b-2
+ Revision: 758135
- remove libtool archive

* Wed Aug 31 2011 Götz Waschk <waschk@mandriva.org> 0.92.1b-1
+ Revision: 697568
- new version
- drop patch

* Wed Aug 24 2011 Götz Waschk <waschk@mandriva.org> 0.92.1-1
+ Revision: 696517
- new version
- fix pkgconfig file

* Sun May 01 2011 Götz Waschk <waschk@mandriva.org> 0.92.0-1
+ Revision: 661304
- new major
- update paths
- new version

* Sun Feb 27 2011 Götz Waschk <waschk@mandriva.org> 0.91.1-1
+ Revision: 640671
- new version
- fix source URL
- remove automake call

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 0.91.0-1mdv2011.0
+ Revision: 581288
- new version
- update file list

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.90.6-2mdv2011.0
+ Revision: 551023
- useless rebuild
- new version
- new URL

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 0.90.5-2mdv2010.1
+ Revision: 503617
- rebuild for new gmp

* Sat Jan 09 2010 Götz Waschk <waschk@mandriva.org> 0.90.5-1mdv2010.1
+ Revision: 487821
- update to new version 0.90.5

* Sat Dec 19 2009 Götz Waschk <waschk@mandriva.org> 0.90.4-1mdv2010.1
+ Revision: 480083
- new version
- fix build

* Fri Nov 13 2009 Götz Waschk <waschk@mandriva.org> 0.90.3-1mdv2010.1
+ Revision: 465682
- new version
- update file list

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 0.90.2-1mdv2010.0
+ Revision: 421336
- update to new version 0.90.2

* Sun Aug 23 2009 Götz Waschk <waschk@mandriva.org> 0.90.1-1mdv2010.0
+ Revision: 420120
- update build deps
- new version
- drop patch

* Sun Jul 05 2009 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2010.0
+ Revision: 392552
- add back require exception

* Sat Jul 04 2009 Funda Wang <fwang@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 392088
- New version 0.90.0

* Wed May 06 2009 Götz Waschk <waschk@mandriva.org> 0.17.4-1mdv2010.0
+ Revision: 372652
- update to new version 0.17.4

* Thu Mar 05 2009 Götz Waschk <waschk@mandriva.org> 0.17.3-1mdv2009.1
+ Revision: 348783
- new version
- update file list

* Wed Feb 25 2009 Götz Waschk <waschk@mandriva.org> 0.17.2-3mdv2009.1
+ Revision: 344871
- fix build

* Sun Nov 23 2008 Götz Waschk <waschk@mandriva.org> 0.17.2-2mdv2009.1
+ Revision: 306113
- fix deps on x86_64

* Sun Nov 23 2008 Götz Waschk <waschk@mandriva.org> 0.17.2-1mdv2009.1
+ Revision: 305960
- new version
- update source URL
- drop patches
- update file list

* Thu Jul 31 2008 Götz Waschk <waschk@mandriva.org> 0.17-9mdv2009.0
+ Revision: 257360
- fix build
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Jul 30 2007 Götz Waschk <waschk@mandriva.org> 0.17-8mdv2008.0
+ Revision: 56648
- fix obsoletes

* Sat Jul 28 2007 Götz Waschk <waschk@mandriva.org> 0.17-7mdv2008.0
+ Revision: 56467
- unpack patch
- fix build
- new devel name
- Import librep

