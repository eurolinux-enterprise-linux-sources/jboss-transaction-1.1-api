%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-transaction-1.1-api
Version:          1.0.1
Release:          5%{dist}
Summary:          Transaction 1.1 API
Group:            Development/Libraries
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-transaction-api_spec.git jboss-transaction-1.1-api
# cd jboss-transaction-1.1-api/ && git archive --format=tar --prefix=jboss-transaction-1.1-api/ jboss-transaction-api_1.1_spec-1.0.1.Final | xz > jboss-transaction-1.1-api-1.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    java-devel
BuildRequires:    jboss-specs-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-ejb-plugin

Requires:         jpackage-utils
Requires:         java
BuildArch:        noarch

%description
The Java Transaction 1.1 API classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Libraries
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-transaction-1.1-api

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-transaction-api_1.1_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc README LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.1-5
- Resolves #961465 - Removed unneeded maven-checkstyle-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Nov 15 2012 Ade Lee <alee@redhat.com> 1.0.1-2
- Removed maven-eclipse-plugin-dependency
- Added maven-clean-plugin

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.20120309git3970b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120309git3970b8
- Packaging after license cleanup upstream

* Mon Oct 24 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-2
- Fixed apidocs issue

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging
