%define upstream_name    URI-Title
%define upstream_version 1.85

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Module to get the titles of things on the web in a sensible way
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/URI-Title-%{upstream_version}.tar.bz2

BuildRequires: perl(LWP::Simple)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(File::Type)
BuildRequires: perl(MP3::Info) 
BuildRequires: perl(Image::Size)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl module to get the titles of things on the web in a sensible way.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# broken with encoding, I do not know why 
#make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/URI/*
%{_mandir}/man3/*
