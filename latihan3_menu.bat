@echo off
:begin
cls
echo Menu Progam:
echo 1. Hello
echo 2. Syistem info
echo 3. Exiy
echo 4. dddd
set /p pilihan=pilihan menu anda:
if %pilihan& == 1 (

 goto 1
 ) else if %pilihan& == 2 (
 goto 2
 ) else if %pilihan& == 3 (
 goto 3
 )

:1
cls
echo ===============================
echo SELAMAT DATANG DIHALAMAN UTAMA
echo ===============================
echo Hi, selamat pagi
pause
goto begin

:2
cls
systeminfo
pause
goto begin

:3
exit
