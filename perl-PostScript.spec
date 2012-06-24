%include	/usr/lib/rpm/macros.perl
Summary:	PostScript perl module
Summary(pl):	Modu� perla PostScript
Name:		perl-PostScript
Version:	0.06
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/PostScript/PostScript-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript - module for generating PostScript documents.

%description -l pl
PostScript - modu� do tworzenia dokument�w w formacie PostScript.

%prep
%setup -q -n PostScript-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz example.pl
%{perl_sitelib}/PostScript/*.pm
%{_mandir}/man3/*
