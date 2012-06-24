Summary:	Utility to copy digital audio cd's
Summary(es):	Extrator de CDs de sonido
Summary(pl):	Program do kopiowania p�yt cd-audio
Summary(pt_BR):	Extrator de CDs de �udio
Summary(ru):	������� ��� ����������� �������� �����-CD
Summary(uk):	���̦�� ��� ��Ц������ �������� ��Ħ�-CD
Name:		cdparanoia-III
Version:	alpha9.8
Release:	8
License:	GPL
Group:		Applications/Sound
Source0:	http://downloads.xiph.org/releases/cdparanoia/%{name}-%{version}.src.tgz
# Source0-md5:	7218e778b5970a86c958e597f952f193
Patch0:		%{name}.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-gcc34.patch
Patch3:		%{name}-libs.patch
URL:		http://www.xiph.org/paranoia/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	cdparanoia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdparanoia (Paranoia III) reads digital audio directly from a CD, then
writes the data to a file or pipe in WAV, AIFC or raw 16 bit linear
PCM format. Cdparanoia's strength lies in its ability to handle a
variety of hardware, including inexpensive drives prone to
misalignment, frame jitter and loss of streaming during atomic reads.
Cdparanoia is also good at reading and repairing data from damaged
CDs.

%description -l es
Cdparanoia (Paranoia III) lee la frecuencia de sonido digital
directamente de un CD, y a partir de �sta escribe los datos en un
archivo o una conexi�n temporal en formato WAV, AIFC o PCM 16 bits. El
poder del Cdparanoia consiste en la capacidad de usar una gran
variedad de hardware, inclusive unidades de accionamiento (drives)
baratos con problemas de alineamiento y que pierden datos durante la
lectura. El Cdparanoia tambi�n sirve para leer y reparar datos de un
CD con defecto.

%description -l pl
CDDA Paranoia czyta z kompaktu w postaci cyfrowej �cie�k� audio, a
nast�pnie zapisuje j� do pliku lub potoku. Formatem zapisu mo�e by�
plik typu WAV, AIFC lub czysty, 16-bitowy PCM.

%description -l pt_BR
Cdparanoia (Paranoia III) l� freq��ncia de �udio digital diretamente
de um CD, e ent�o escreve os dados para um arquivo ou pipe em formato
WAV, AIFC ou PCM 16 bits. O poder do Cdparanoia est� na capacidade de
usar uma grande variedade de hardware, inclusive drives baratos com
problemas de alinhamento e que perdem dados durante a leitura. O
Cdparanoia tamb�m � bom para ler e reparar dados de um CD danificado.

%description -l ru
Cdparanoia (Paranoia III) ������ �������� ����� �������� � CD,
��������� ������ � ���� ��� ����� � �������� WAV, AIFC ��� raw 16 bit
linear PCM. ������� ������� Cdparanoia - � ����������� �������� �
������������� ���������� ������������, ������� ������� ���������,
�������� � misalignment, frame jitter � loss of streaming during
atomic reads. Cdparanoia ����� ������ ����������� � ������� �
������������ ������ � ������������ CD.

%description -l uk
Cdparanoia (Paranoia III) ����� ������� ��Ħ� ������� � CD �� �����դ
��Φ � ���� �� ����� � �������� WAV, AIFC �� raw 16 bit linear PCM.
������ ������� Cdparanoia - � ��������Ԧ ��������� � Ҧ�����Φ����
��������� �������������, ��������� ����צ ���������, �����Φ ��
misalignment, frame jitter �� loss of streaming during atomic reads.
Cdparanoia ����� ����� ������Ѥ���� � �������� �� ������������ ����� �
����������� CD.

%package libs
Summary:	Libraries of CD Paranoia program
Summary(pl):	Biblioteki programu CD Paranoia
Group:		Libraries
Obsoletes:	cdparanoia-libs

%description libs
This package contains libraries of CD Paranoia program.

%description libs -l pl
W pakiecie tym znajduj� si� biblioteki programu CD Paranoia.

%package devel
Summary:	Header files for CD Paranoia libraries
Summary(pl):	Pliki nag��wkowe do bibliotek programu CD Paranoia
Summary(pt_BR):	Bibliotecas de desenvolvimento para o cdparanoia
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	cdparanoia-devel

%description devel
This package contains header files for CD Paranoia libraries.

%description devel -l pl
W pakiecie tym znajduj� si� pliki nag��wkowe do bibliotek programu CD
Paranoia.

%description devel -l pt_BR
Arquivos de inclus�o e bibliotecas necess�rias para desenvolver
programas que utilizam o cdparanoia.

%package static
Summary:	Static libraries of CD Paranoia program
Summary(pl):	Biblioteki statyczne programu CD Paranoia
Summary(pt_BR):	Bibliotecas est�ticas do cdparanoia
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries of CD Paranoia program.

%description static -l pl
Biblioteki statyczne programu CD Paranoia.

%description static -l pt_BR
Bibliotecas est�ticas do cdparanoia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# bleh? look at the beginning of configure.in
cp -f %{_datadir}/automake/config.guess configure.guess
cp -f %{_datadir}/automake/config.sub configure.sub
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1,%{_includedir}}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}

install -d $RPM_BUILD_ROOT%{_mandir}/ja/man1
install cdparanoia.1.jp $RPM_BUILD_ROOT%{_mandir}/ja/man1

# for rpm autodeps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*so.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README FAQ.txt
%attr(755,root,root) %{_bindir}/cdparanoia
%{_mandir}/man?/*
%lang(ja) %{_mandir}/ja/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
