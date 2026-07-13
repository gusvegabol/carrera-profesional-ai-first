@echo off
setlocal EnableExtensions

if not defined OLLAMA_BASE_URL (
    set "OLLAMA_BASE_URL=http://localhost:11434/v1"
) else if /I "%OLLAMA_BASE_URL:~-3%"=="/v1" (
    rem La URL ya es compatible con Graphify.
) else (
    set "OLLAMA_BASE_URL=%OLLAMA_BASE_URL%/v1"
)

rem Cada directorio se procesa como un corpus documental independiente.
rem No ejecutar Graphify sobre la raiz del repositorio: mezclar corpus
rem produciria relaciones artificiales y recuperacion de contexto irrelevante.
rem Corpus metodologico y operativo de entrevista.
echo "Iniciando graphify en boveda-entrevista-profesional ..."
cd "C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first\boveda-entrevista-profesional"
graphify update .
graphify extract . --backend ollama
echo " "
echo " "
echo " "
echo "Iniciando graphify en docs/ ..."
rem Corpus funcional, metodologico y de debate documental.
cd "C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first\docs"
graphify update .
graphify extract . --backend ollama
echo " "
echo " "
echo " "
echo "Iniciando graphify en .pcs/ ..."
rem Corpus funcional, metodologico y de debate documental.
cd "C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first\.pcs"
graphify update .
graphify extract . --backend ollama
echo " "
echo " "
echo " "

endlocal
pause
