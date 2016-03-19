%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	A text hyphenation library
Name:		hyphen
Version:	2.8.6
Release:	12
Group:		System/Libraries 
License:	LGPLv2+
Url:		http://hunspell.sf.net
Source0:	http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz

BuildRequires:	perl
BuildRequires:	libtool

%description
Hyphen is a library for high quality hyphenation and justification.

%package -n %{libname}
Summary:	Files for developing with hyphen
Group:		System/Libraries 
Suggests:	%{name}-en = %{version}-%{release}
Provides:	hyphen

%description -n %{libname}
Hyphen is a library for high quality hyphenation and justification.

%package -n %{devname}
Summary:	Files for developing with hyphen
Group:		Development/C 
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Includes and definitions for developing with hyphen

%package en
Summary:	English hyphenation rules
Group:		Text tools 
BuildArch:	noarch

%description en
English hyphenation rules.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%check
%make check

%install
%makeinstall_std

pushd %{buildroot}/%{_datadir}/hyphen/
en_US_aliases="en_AG en_AU en_BS en_BW en_BZ en_CA en_DK en_GB en_GH en_HK en_IE en_IN en_JM en_NA en_NZ en_PH en_SG en_TT en_ZA en_ZW"
for lang in $en_US_aliases; do
        ln -s hyph_en_US.dic hyph_$lang.dic
done
popd

%files -n %{libname}
%{_libdir}/libhyphen.so.%{major}*

%files en
%dir %{_datadir}/hyphen
%{_datadir}/hyphen/hyph_en*.dic

%files -n %{devname}
%doc AUTHORS ChangeLog README README.hyphen README.nonstandard TODO
%{_bindir}/substrings.pl
%{_includedir}/hyphen.h
%{_libdir}/*.so

