Summary:	rcorder prints a dependency ordering of interdependent files
Summary(pl):	rcorder - wypisywanie kolejno¶ci zale¿no¶ci wspó³zale¿nych plików
Name:		rcorder
Version:	20040522
Release:	0.1
Epoch:		0
License:	BSD
Group:		Applications/Text
Source0:	http://test.mmt.pl/pld/rcorder/%{name}-%{version}.tar.gz
# Source0-md5:	4bad517b3b8809cf1994dea0c76e4002
URL:		http://www.freebsd.org/cgi/cvsweb.cgi/src/sbin/rcorder/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.8.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rcorder utility is designed to print out a dependency ordering of
a set of interdependent files.  Typically it is used to find an
execution sequence for a set of shell scripts in which certain files
must be executed before others. rcorder comes from NetBSD. NetBSD and
FreeBSD use it for ordering start sequence in their boot scripts.
This package is a Linux port.

%description -l pl
Rcorder wypisuje kolejno¶æ zale¿no¶ci wspó³zale¿nych plików. Zazwyczaj
jest u¿ywany do znajdywania prawid³owej sekwencji uruchamiania
skryptów, w których kolejno¶æ uruchamiania jest wa¿na. Narzêdzie to
wywodzi siê z NetBSD gdzie, tak jak we FreeBSD, jest u¿ywane do
ustalania kolejno¶ci uruchamiania us³ug podczas startu systemu. Ten
pakiet zawiera port linuksowy.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/rcorder $RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSES
%attr(755,root,root) /sbin/*
%{_mandir}/man?/*
