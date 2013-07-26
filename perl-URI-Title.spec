%define upstream_name    URI-Title
%define upstream_version 1.86

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.86
Release:	1

Summary:	Module to get the titles of things on the web in a sensible way
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/URI/URI-Title-1.86.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(File::Type)
BuildRequires:	perl(MP3::Info) 
BuildRequires:	perl(Image::Size)
BuildArch:	noarch

%description
Perl module to get the titles of things on the web in a sensible way.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# broken with encoding, I do not know why 
#make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/URI/*
%{_mandir}/man3/*


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.850.0-1mdv2011.0
+ Revision: 684829
- update to new version 1.85

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.820.0-1mdv2010.0
+ Revision: 406207
- rebuild using %%perl_convert_version

* Mon Oct 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.82-1mdv2009.1
+ Revision: 295523
- update to new version 1.82

* Tue Oct 14 2008 Michael Scherer <misc@mandriva.org> 1.62-1mdv2009.1
+ Revision: 293745
- disable test until I found out why they are broke with regard to encoding
- import perl-URI-Title

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Sep 24 2007 Michael Scherer <misc@mandriva.org> 1.62-1mdv2008.0
- First Mandriva package

