Summary:	uqwk creates packages with mail and/or news for offline reading
Summary(pl):	uqwk tworzy paczki z poczt± i/lub newsami do czytania offline
Name:		uqwk
Version:	2.21
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.xs4all.nl/~js/warez/%{name}-%{version}.tar.gz
# Source0-md5:	2dbaab71f088e7fd8bb5472c9946e963
Source1:	%{name}-config_pld.h
Patch0:		%{name}-no_libnsl.patch
URL:		http://www.xs4all.nl/~js/warez/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uqwk is a program which collects all a user's unread mail or news and
formats it into a packet for offline reading. QWK, Simple Offline
Usenet Packet (SOUP), and ZipNews packet formats are supported.

%description -l pl
uqwk jest programem który zbiera ca³± nieprzeczytan± pocztê lub
wiadomo¶ci usenetowe, i uk³ada je w pakiet do czytania offline.
Obs³ugiwane s± formaty QWK, Simple Offline Usenet Packet (SOUP) i
ZipNews.

%prep
%setup  -q
%patch0 -p1
install %{SOURCE1} config-pld.h

%build
%{__autoconf}
%configure \
	--with-config=config-pld.h

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install uqwk $RPM_BUILD_ROOT%{_bindir}
install uqwk.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc scripts README HISTORY FAQ README.Typhoon
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
