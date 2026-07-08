echo off
echo "Iniciando graphify ..."
cd "C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first\boveda-entrevista-profesional"
graphify update .
graphify extract . --backend ollama
echo " "
echo " " 
echo " "
pause