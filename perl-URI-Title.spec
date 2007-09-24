%define realname   URI-Title

Name:		perl-%{realname}
Version:    1.62
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Module to get the titles of things on the web in a sensible way
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/URI-Title-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(Module::Pluggable)
BuildArch: noarch

%description
Perl module to get the titles of things on the web in a sensible way.

%prep
%setup -q -n URI-Title-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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

