Summary:	Utility to copy digital audio cd's
Summary(es.UTF-8):	Extrator de CDs de sonido
Summary(pl.UTF-8):	Program do kopiowania płyt cd-audio
Summary(pt_BR.UTF-8):	Extrator de CDs de áudio
Summary(ru.UTF-8):	Утилита для копирования цифровых аудио-CD
Summary(uk.UTF-8):	Утиліта для копіювання цифрових аудіо-CD
Name:		cdparanoia-III
Version:	10.2
Release:	3
Epoch:		2
License:	LGPL v2 (libraries), GPL v2 (utility)
Group:		Applications/Sound
Source0:	http://downloads.xiph.org/releases/cdparanoia/%{name}-%{version}.src.tgz
# Source0-md5:	b304bbe8ab63373924a744eac9ebc652
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-gcc43.patch
Patch2:		%{name}-buffer.patch
Patch3:		%{name}-fpic.patch
URL:		http://www.xiph.org/paranoia/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
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

%description -l es.UTF-8
Cdparanoia (Paranoia III) lee la frecuencia de sonido digital
directamente de un CD, y a partir de ésta escribe los datos en un
archivo o una conexión temporal en formato WAV, AIFC o PCM 16 bits. El
poder del Cdparanoia consiste en la capacidad de usar una gran
variedad de hardware, inclusive unidades de accionamiento (drives)
baratos con problemas de alineamiento y que pierden datos durante la
lectura. El Cdparanoia también sirve para leer y reparar datos de un
CD con defecto.

%description -l pl.UTF-8
CDDA Paranoia czyta z kompaktu w postaci cyfrowej ścieżkę audio, a
następnie zapisuje ją do pliku lub potoku. Formatem zapisu może być
plik typu WAV, AIFC lub czysty, 16-bitowy PCM.

%description -l pt_BR.UTF-8
Cdparanoia (Paranoia III) lê freqüência de áudio digital diretamente
de um CD, e então escreve os dados para um arquivo ou pipe em formato
WAV, AIFC ou PCM 16 bits. O poder do Cdparanoia está na capacidade de
usar uma grande variedade de hardware, inclusive drives baratos com
problemas de alinhamento e que perdem dados durante a leitura. O
Cdparanoia também é bom para ler e reparar dados de um CD danificado.

%description -l ru.UTF-8
Cdparanoia (Paranoia III) читает цифровое аудио напрямую с CD,
записывая данные в файл или канал в форматах WAV, AIFC или raw 16 bit
linear PCM. Сильная сторона Cdparanoia - в возможности работать с
разнообразным аппаратным обеспечением, включая дешевые дисководы,
склонные к misalignment, frame jitter и loss of streaming during
atomic reads. Cdparanoia также хорошо справляется с чтением и
исправлением данных с поврежденных CD.

%description -l uk.UTF-8
Cdparanoia (Paranoia III) читає цифрове аудіо напряму з CD та записує
дані в файл чи канал в форматах WAV, AIFC чи raw 16 bit linear PCM.
Сильна сторона Cdparanoia - в можливості працювати з різноманітним
апаратним забезпеченням, включаючи дешеві дисководи, схильні до
misalignment, frame jitter та loss of streaming during atomic reads.
Cdparanoia також добре справляється з читанням та виправленням даних з
пошкоджених CD.

%package libs
Summary:	Libraries of CD Paranoia program
Summary(pl.UTF-8):	Biblioteki programu CD Paranoia
License:	LGPL v3
Group:		Libraries
Obsoletes:	cdparanoia-libs

%description libs
This package contains libraries of CD Paranoia program.

%description libs -l pl.UTF-8
W pakiecie tym znajdują się biblioteki programu CD Paranoia.

%package devel
Summary:	Header files for CD Paranoia libraries
Summary(pl.UTF-8):	Pliki nagłówkowe do bibliotek programu CD Paranoia
Summary(pt_BR.UTF-8):	Bibliotecas de desenvolvimento para o cdparanoia
License:	LGPL v3
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	cdparanoia-devel

%description devel
This package contains header files for CD Paranoia libraries.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe do bibliotek programu CD
Paranoia.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão e bibliotecas necessárias para desenvolver
programas que utilizam o cdparanoia.

%package static
Summary:	Static libraries of CD Paranoia program
Summary(pl.UTF-8):	Biblioteki statyczne programu CD Paranoia
Summary(pt_BR.UTF-8):	Bibliotecas estáticas do cdparanoia
License:	LGPL v3
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libraries of CD Paranoia program.

%description static -l pl.UTF-8
Biblioteki statyczne programu CD Paranoia.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas do cdparanoia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
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

install -D cdparanoia.1.jp $RPM_BUILD_ROOT%{_mandir}/ja/man1/cdparanoia.1

# for rpm autodeps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*so.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/cdparanoia
%{_mandir}/man1/cdparanoia.1*
%lang(ja) %{_mandir}/ja/man1/cdparanoia.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdda_interface.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcdda_interface.so.0
%attr(755,root,root) %{_libdir}/libcdda_paranoia.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcdda_paranoia.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdda_interface.so
%attr(755,root,root) %{_libdir}/libcdda_paranoia.so
%{_includedir}/cdda_interface.h
%{_includedir}/cdda_paranoia.h
%{_includedir}/utils.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcdda_interface.a
%{_libdir}/libcdda_paranoia.a
