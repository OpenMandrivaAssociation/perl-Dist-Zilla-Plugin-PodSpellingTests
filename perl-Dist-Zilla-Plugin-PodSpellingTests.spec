%define upstream_name    Dist-Zilla-Plugin-PodSpellingTests
%define upstream_version 1.101420

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Release tests for POD spelling
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Pod::Wordlist::hanekomu)
BuildRequires:	perl(Test::More) >= 0.940.0
BuildRequires:	perl(Test::Spelling)

BuildArch:	noarch

%description
This is an extension of the Dist::Zilla::Plugin::InlineFiles manpage,
providing the following files

  xt/release/pod-spell.t - a standard Test::Spelling test

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*

