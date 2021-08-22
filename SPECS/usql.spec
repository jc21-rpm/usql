%define debug_package %{nil}

%global gh_user xo

Name:           usql
Version:        0.9.3
Release:        1%{?dist}
Summary:        Universal command-line interface for SQL databases 
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz

%description
usql is a universal command-line interface for PostgreSQL, MySQL, Oracle
Database, SQLite3, Microsoft SQL Server, and many other databases including
NoSQL and non-relational databases!

%prep
%setup -q -n %{name}-%{version}

%build
CGO_ENABLED=on GO111MODULE=on go build -tags most -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Aug 23 2021 Jamie Curnow <jc@jc21.com> 0.9.3-1
- https://github.com/xo/usql/releases/tag/v0.9.3

* Thu Jul 8 2021 Jamie Curnow <jc@jc21.com> 0.9.2-1
- https://github.com/xo/usql/releases/tag/v0.9.2

