@echo off
rem Script d'installation de la bibliothèque requests en utilisant pip

rem Assurez-vous que pip est installé
python -m pip --version > install_files/installation_log.txt 2>&1
if %errorlevel% neq 0 (
    echo "pip pour python n'est pas installe. Installation en cours..."
    python install_files/get-pip.py >> install_files/installation_log.txt 2>&1
    if %errorlevel% neq 0 (
        echo "L'installation de pip a echoue. Veuillez installer pip manuellement."
        pause
        exit /b 1
    )
)

rem Installez la bibliothèque requests
echo "Installation des fichiers necessaires."
python -m pip install requests >> install_files/installation_log.txt 2>&1
if %errorlevel% neq 0 (
    echo "L'installation de la librairie requests pour python a echoue. Veuillez verifier votre connexion Internet et reessayer."
    pause
    exit /b 1
)

echo "Installation terminee avec succes. Merci de quitter cette page."
pause
