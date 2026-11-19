#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Tree
%define	pnam	Simple-VisitorFactory
Summary:	Tree::Simple::VisitorFactory - A factory object for dispensing Visitor objects
Summary(pl.UTF-8):	Tree::Simple::VisitorFactory - obiekt tworzący do rozdzielania obiektów Visitor
Name:		perl-Tree-Simple-VisitorFactory
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/R/RS/RSAVAGE/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	9bf9a85d493fe92397b7c483797646b4
URL:		https://metacpan.org/dist/Tree-Simple-VisitorFactory/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Tree-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tree::Simple::VisitorFactory is a factory for dispensing
Tree::Simple::Visitor::* objects.

%description -l pl.UTF-8
Tree::Simple::VisitorFactory to obiekt tworzący do rozdzielania
obiektów Tree::Simple::Visitor::*.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README LICENSE
%{perl_vendorlib}/Tree/Simple/*.pm
%{perl_vendorlib}/Tree/Simple/Visitor
%{_mandir}/man3/*
