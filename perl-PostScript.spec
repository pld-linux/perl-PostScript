%include	/usr/lib/rpm/macros.perl
Summary:	PostScript perl module
Summary(pl):	Modu³ perla PostScript
Name:		perl-PostScript
Version:	0.06
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/PostScript/PostScript-%{version}.tar.gz
# Source0-md5:	2a91cc23f2d8958e063f7ff09163faa0
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript - module for generating PostScript documents.

%description -l pl
PostScript - modu³ do tworzenia dokumentów w formacie PostScript.

%prep
%setup -q -n PostScript-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *txt
%{perl_vendorlib}/PostScript/*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
