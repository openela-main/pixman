%define gitdate 20070827
%define gitrev 8ff7213f39edc1b2b8b60d6b0cc5d5f14ca1928d

Name:           pixman
Version:        0.38.4
Release:        3%{?dist}
Summary:        Pixel manipulation library

Group:          System Environment/Libraries
License:        MIT
URL:            https://gitlab.freedesktop.org/pixman/pixman
#VCS:           git:git://git.freedesktop.org/git/pixman
# To make git snapshots:
# ./make-pixman-snapshot.sh %{\?gitrev}
# if no revision specified, makes a new one from HEAD.
Source0:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Source1:        make-pixman-snapshot.sh

Patch0: 0001-Initialize-temporary-buffers-in-general_composite_re.patch
Patch1: 0001-Avoid-integer-overflow-leading-to-out-of-bounds-writ.patch

BuildRequires:  automake autoconf libtool
BuildRequires:  gcc

%description
Pixman is a pixel manipulation library for X and Cairo.

%package devel
Summary: Pixel manipulation library development package
Group: Development/Libraries
Requires: %{name}%{?isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development library for pixman.

%prep
%autosetup -p1

%build
%configure \
%ifarch %{arm}
  --disable-arm-iwmmxt --disable-arm-iwmmxt2 \
%endif
  --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT

find %{buildroot} -type f -name "*.la" -delete

%check
make check %{?_smp_mflags} V=1

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING
%{_libdir}/libpixman-1*.so.*

%files devel
%dir %{_includedir}/pixman-1
%{_includedir}/pixman-1/pixman.h
%{_includedir}/pixman-1/pixman-version.h
%{_libdir}/libpixman-1*.so
%{_libdir}/pkgconfig/pixman-1.pc

%changelog
* Mon Oct 09 2023 José Expósito <jexposit@redhat.com> - 0.38.4-3
- Backport fix for CVE-2022-44638

* Tue Feb 22 2022 Adam Jackson <ajax@redhat.com> - 0.38.4-2
- Backport the pixman part of cairo CVE-2020-35492

* Tue Nov 19 2019 Adam Jackson <ajax@redhat.com> - 0.38.4-1
- pixman 0.38.4

* Thu Nov 29 2018 Adam Jackson <ajax@redhat.com> - 0.36.0-1
- pixman 0.36.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 0.34.0-9
- Use ldconfig scriptlet macros

* Fri May 04 2018 Dan Horák <dan[at]danny.cz> - 0.34.0-8
- fix vector loads in VMX (ppc64le) (#1572540)

* Thu Apr 26 2018 Adam Jackson <ajax@redhat.com> - 0.34.0-7
- Enable %%check
- --disable-vmx to fix %%check failures with gcc8
- Remove stray --disable-ssse3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 <oded.gabbay@gmail.com> - 0.34.0-1
- Update to 0.34.0 (#1249357)

* Tue Dec 22 2015 Oded Gabbay <oded.gabbay@gmail.com> 0.33.6-1
- pixman 0.33.6

* Fri Oct 23 2015 Oded Gabbay <oded.gabbay@gmail.com> 0.33.4-1
- pixman 0.33.4

* Sun Aug 09 2015 Oded Gabbay <oded.gabbay@gmail.com> 0.33.2-1
- pixman 0.33.2
- Enable VMX fast paths on ppc64le now that they are fixed

* Tue Jun 16 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.32.6-6
- revert cflag option added in -5 the broke building

* Mon May 11 2015 Adam Jackson <ajax@redhat.com> 0.32.6-5
- Fix devel's requirement on the base package to include %%{?isa}

* Mon Nov 10 2014 Adam Jackson <ajax@redhat.com> 0.32.6-4
- Disable (broken) VMX fast paths on ppc64le for now.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.32.6-2
- Enable make check but don't (currently) fail the build on failure
- Include COPYING as per packaging guidelines
- Minor spec cleanups

* Sun Jul 06 2014 Soren Sandmann <soren.sandmann@gmail.com> 0.32.6-1
- pixman 0.32.6
- drop SSSE3 patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 14 2013 Soren Sandmann <ssp@redhat.com> 0.32.0-2
- Add patch to fix SSSE3 detection

* Sun Nov 10 2013 Soren Sandmann <ssp@redhat.com> 0.32.0-1
- pixman 0.32.0

* Sat Nov 2 2013 Soren Sandmann <ssp@redhat.com> 0.31.2-1
- pixman 0.31.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Karsten Hopp <karsten@redhat.com> 0.30.0-2
- bump release and rebuild to fix dependencies on PPC

* Wed May 8 2013 Soren Sandmann <ssp@redhat.com> 0.30.0-1
- pixman 0.30.0
