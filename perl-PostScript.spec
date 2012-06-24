%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	PostScript perl module
Summary(pl):	Modu� perla PostScript
Name:		perl-PostScript
Version:	0.05
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/PostScript/PostScript-%{version}.tar.gz
Patch:		perl-PostScript-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
PostScript - module for generating PostScript documents.

%description -l pl
PostScript - modu� do tworzenia dokument�w w formacie PostScript.

%prep
%setup -q -n PostScript-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/PostScript/Metrics
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,example.txt}.gz example.pl

%{perl_sitelib}/PostScript/*.pm
%{perl_sitearch}/auto/PostScript/Metrics

%{_mandir}/man3/*
