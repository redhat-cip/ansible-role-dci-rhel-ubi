%define _source_payload w0.gzdio
%define _binary_payload w0.gzdio

Name:       ansible-role-dci-rhel-ubi
Version:    0.0.1
Release:    1%{?dist}
Summary:    ansible-role-dci-rhel-ubi
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-rhel-ubi
Source0:    ansible-role-dci-rhel-ubi-%{version}.tar.gz

BuildArch:  noarch

%description
An Ansible role that is used to automate ubi mirroring

%prep
%setup -qc


%build

%install
mkdir -p %{buildroot}%{_datadir}/dci/roles/dci-rhel-ubi
chmod 755 %{buildroot}%{_datadir}/dci/roles/dci-rhel-ubi

cp -r library %{buildroot}%{_datadir}/dci/roles/dci-rhel-ubi
cp -r tasks %{buildroot}%{_datadir}/dci/roles/dci-rhel-ubi
cp -r defaults %{buildroot}%{_datadir}/dci/roles/dci-rhel-ubi
cp -r vars %{buildroot}%{_datadir}/dci/roles/dci-rhel-ubi
cp -r templates %{buildroot}%{_datadir}/dci/roles/dci-rhel-ubi
cp -r filter_plugins %{buildroot}%{_datadir}/dci/roles/dci-rhel-ubi

%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-rhel-ubi


%changelog
* Wed Jul 29 2020 Bill Peck <bpeck@redhat.com> - 0.0.1-1
- Initial release
