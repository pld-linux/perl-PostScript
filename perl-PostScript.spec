%include	/usr/lib/rpm/macros.perl
Summary:	PostScript perl module
Summary(pl):	Modu³ perla PostScript
Name:		perl-PostScript
Version:	0.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/PostScript/PostScript-%{version}.tar.gz
Patch0:		perl-PostScript-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript - module for generating PostScript documents.

%description -l pl
PostScript - modu³ do tworzenia dokumentów w formacie PostScript.

%prep
%setup -q -n PostScript-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
