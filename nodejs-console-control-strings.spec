%{?scl:%scl_package nodejs-console-control-strings}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name console-control-strings

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    1.1.0
Release:    2%{?dist}
Summary:    A library of cross-platform tested terminal/console command strings for doing things like color and cursor positioning
License:    ISC
URL:        https://github.com/iarna/console-control-strings
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
A library of cross-platform tested terminal/console command strings for doing things like color and cursor positioning.  This is a subset of both ansi and vt100.  All control codes included work on both Windows & Unix-like OSes, except where noted.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-2
- Initial build

