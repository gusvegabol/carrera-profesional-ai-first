echo off
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

pause
