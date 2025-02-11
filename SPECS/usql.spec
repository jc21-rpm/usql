%define debug_package %{nil}

%global gh_user xo

Name:           usql
Version:        0.19.17
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
CGO_ENABLED=on GO111MODULE=on go build -tags 'most sqlite_app_armor sqlite_fts5 sqlite_introspect sqlite_json1 sqlite_stat4 sqlite_userauth sqlite_vtable sqlite_icu no_adodb' -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Feb 22 2025 Jamie Curnow <jc@jc21.com> 0.19.17-1
- https://github.com/xo/usql/releases/tag/v0.19.17

* Tue Jan 14 2025 Jamie Curnow <jc@jc21.com> 0.19.16-1
- https://github.com/xo/usql/releases/tag/v0.19.16

* Mon Dec 9 2024 Jamie Curnow <jc@jc21.com> 0.19.14-1
- https://github.com/xo/usql/releases/tag/v0.19.14

* Fri Oct 25 2024 Jamie Curnow <jc@jc21.com> 0.19.12-1
- https://github.com/xo/usql/releases/tag/v0.19.12

* Tue Oct 22 2024 Jamie Curnow <jc@jc21.com> 0.19.4-1
- https://github.com/xo/usql/releases/tag/v0.19.4

* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> 0.19.3-1
- https://github.com/xo/usql/releases/tag/v0.19.3

* Wed May 22 2024 Jamie Curnow <jc@jc21.com> 0.19.1-1
- https://github.com/xo/usql/releases/tag/v0.19.1

* Thu Jan 4 2024 Jamie Curnow <jc@jc21.com> 0.17.4-1
- https://github.com/xo/usql/releases/tag/v0.17.4

* Thu Aug 17 2023 Jamie Curnow <jc@jc21.com> 0.15.0-1
- https://github.com/xo/usql/releases/tag/v0.15.0

* Wed Jul 19 2023 Jamie Curnow <jc@jc21.com> 0.14.12-1
- https://github.com/xo/usql/releases/tag/v0.14.12

* Tue Jul 4 2023 Jamie Curnow <jc@jc21.com> 0.14.10-1
- https://github.com/xo/usql/releases/tag/v0.14.10

* Tue Jun 6 2023 Jamie Curnow <jc@jc21.com> 0.14.8-1
- https://github.com/xo/usql/releases/tag/v0.14.8

* Thu Mar 9 2023 Jamie Curnow <jc@jc21.com> 0.13.10-1
- https://github.com/xo/usql/releases/tag/v0.13.10

* Fri Feb 3 2023 Jamie Curnow <jc@jc21.com> 0.13.8-1
- https://github.com/xo/usql/releases/tag/v0.13.8

* Thu Jan 5 2023 Jamie Curnow <jc@jc21.com> 0.13.5-1
- https://github.com/xo/usql/releases/tag/v0.13.5

* Tue Jan 3 2023 Jamie Curnow <jc@jc21.com> 0.13.4-1
- https://github.com/xo/usql/releases/tag/v0.13.4

* Mon Nov 14 2022 Jamie Curnow <jc@jc21.com> 0.13.1-1
- https://github.com/xo/usql/releases/tag/v0.13.1

* Mon Sep 12 2022 Jamie Curnow <jc@jc21.com> 0.12.13-1
- https://github.com/xo/usql/releases/tag/v0.12.13

* Thu Aug 4 2022 Jamie Curnow <jc@jc21.com> 0.11.12-1
- https://github.com/xo/usql/releases/tag/v0.11.12

* Wed Aug 3 2022 Jamie Curnow <jc@jc21.com> 0.11.1-1
- https://github.com/xo/usql/releases/tag/v0.11.1

* Tue Aug 31 2021 Jamie Curnow <jc@jc21.com> 0.9.4-1
- https://github.com/xo/usql/releases/tag/v0.9.4

* Mon Aug 23 2021 Jamie Curnow <jc@jc21.com> 0.9.3-1
- https://github.com/xo/usql/releases/tag/v0.9.3

* Thu Jul 8 2021 Jamie Curnow <jc@jc21.com> 0.9.2-1
- https://github.com/xo/usql/releases/tag/v0.9.2

