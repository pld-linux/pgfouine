Summary:	PgFouine PostgreSQL log analyzer
Name:		pgfouine
Version:	1.0
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://pgfouine.projects.postgresql.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	a6c10e69582f7beef74e8de9313675e9
Patch0:		%{name}-include_path.patch
URL:		http://pgfouine.projects.postgresql.org/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	tar >= 1:1.15.1
Requires:	php(gd)
Requires:	php-cli
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pgFouine is a PostgreSQL log analyzer. It generates text or HTML
reports from PostgreSQL log files. These reports contain the list of
the slowest queries, the queries that take the most time and so on.

pgFouine can also:
- analyze VACUUM VERBOSE output to help you improve your VACUUM
  strategy,
- generate Tsung sessions file to benchmark your PostgreSQL server.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT/%{_bindir}

for i in include version.php; do
	cp -rp $i $RPM_BUILD_ROOT/%{_datadir}/%{name}/
done

install pgfouine.php $RPM_BUILD_ROOT/%{_bindir}/
install pgfouine_vacuum.php $RPM_BUILD_ROOT/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING THANKS README rpm-specific/sources/pgfouine-tutorial.txt
%attr(755,root,root) %{_bindir}/pgfouine.php
%attr(755,root,root) %{_bindir}/pgfouine_vacuum.php
%{_datadir}/%{name}