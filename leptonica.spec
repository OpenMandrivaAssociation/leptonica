%define major 5
%define libname %mklibname lept %{major}
%define devname %mklibname -d lept

Summary:	C library for image processing and image analysis operations
Name:		leptonica
Version:	1.78.0
Release:	2
License:	MIT
Group:		Graphics
Url:		http://www.leptonica.org
Source0:	http://www.leptonica.org/source/%{name}-%{version}.tar.gz
BuildRequires:	giflib-devel
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)

%description
Well-tested C code for some basic image processing operations, along with
a description of the functions and some design methods. A full set of affine
transformations (translation, shear, rotation, scaling) on images of all depths
is included, with the exception that some of the scaling methods do not work
at all depths. There are also implementations of binary morphology, grayscale
morphology, convolution and rank order filters, and applications such as jbig2
image processing and color quantization.

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

%package -n %{devname}
Summary:	C library for image processing and image analysis operations
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n %{devname}
This package contains development files only.

%prep
%setup -q

%build
sed -i 's/EGifOpenFileHandle(fd))/EGifOpenFileHandle(fd, NULL))/g' src/gifio.c
sed -i 's/DGifOpenFileHandle(fd))/DGifOpenFileHandle(fd, NULL))/g' src/gifio.c
#% configure2_5x --disable-static --disable-programs
%configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-programs \
	--disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/liblept.so.%{major}*

%files -n %{devname}
%doc leptonica-license.txt README.html
%{_libdir}/*.so
%{_includedir}/leptonica
%{_libdir}/pkgconfig/lept.pc

