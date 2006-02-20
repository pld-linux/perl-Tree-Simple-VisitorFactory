#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	Simple-VisitorFactory
Summary:	Tree::Simple::VisitorFactory - A factory object for dispensing Visitor objects
Summary(pl):	Tree::Simple::VisitorFactory - obiekt tworz±cy do rozdzielania obiektów Visitor
Name:		perl-Tree-Simple-VisitorFactory
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff7803a452e7fb188c71048cc2f69f6e
URL:		http://search.cpan.org/dist/Tree-Simple-VisitorFactory/
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

%description -l pl
Tree::Simple::VisitorFactory to obiekt tworz±cy do rozdzielania
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
%doc Changes README
%{perl_vendorlib}/Tree/Simple/*.pm
%{perl_vendorlib}/Tree/Simple/Visitor
%{_mandir}/man3/*
