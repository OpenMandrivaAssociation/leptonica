# exclude unwanter cmake requires
%global __requires_exclude cmake\\(openjpeg\\)|cmake\\(OpenJPEG\\) \
	|cmake\\(webp\\)|cmake\\(WebP\\)

%define major 6
%define libname %mklibname leptonica
%define devname %mklibname -d leptonica

%bcond_without	prog

Summary:	C library for image processing and image analysis operations
Name:		leptonica
Version:	1.84.1
Release:	1
License:	MIT
Group:		Graphics
Url:		http://www.leptonica.org
Source0:	https://github.com/DanBloomberg/leptonica/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake ninja
BuildRequires:	giflib-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
# (fedora)
Patch0:		leptonica_cmake.patch

%description
Well-tested C code for some basic image processing operations, along with
a description of the functions and some design methods. A full set of affine
transformations (translation, shear, rotation, scaling) on images of all depths
is included, with the exception that some of the scaling methods do not work
at all depths. There are also implementations of binary morphology, grayscale
morphology, convolution and rank order filters, and applications such as jbig2
image processing and color quantization.

%if %{with prog}
%files
%{_bindir}/*
%endif

#----------------------------------------------------------------------------

%package -n %{libname} 
Summary:	C library for image processing and image analysis operations

%description -n %{libname}
Well-tested C code for some basic image processing operations, along with
a description of the functions and some design methods. A full set of affine
transformations (translation, shear, rotation, scaling) on images of all depths
is included, with the exception that some of the scaling methods do not work
at all depths. There are also implementations of binary morphology, grayscale
morphology, convolution and rank order filters, and applications such as jbig2
image processing and color quantization.

%files -n %{libname}
%{_libdir}/libleptonica.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	C library for image processing and image analysis operations
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n %{devname}
This package contains development files only.

%files -n %{devname}
%doc leptonica-license.txt README.html
%{_libdir}/*.so
%{_includedir}/leptonica
%{_libdir}/pkgconfig/lept*.pc
%{_libdir}/cmake/%{name}/*.cmake

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_PROG:BOOL=%{?with_prog:ON}%{!?with_prog:OFF} \
	-DSYM_LINK:BOOL=OFF \
	-GNinja
%ninja_build

%install
%ninja_install -C build
#ln -s lept_RelWithDebInfo.pc %{buildroot}%{_libdir}/pkgconfig/lept.pc
#ln -s lept_RelWithDebInfo.pc %{buildroot}%{_libdir}/pkgconfig/lept_Release.pc
#ln -s lept_RelWithDebInfo.pc %{buildroot}%{_libdir}/pkgconfig/lept_Debug.pc
