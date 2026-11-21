# Evaluación: Git y GitHub (Fundamentos)

## Evaluación: Opción Múltiple (1/2)

**1. ¿Qué comando mueve cambios al staging area?**
* **Respuesta:** **b) `git add`**
* **Explicación:** `git add` prepara y agrupa los cambios modificados o nuevos para incluirlos en el próximo commit.

**2. ¿Qué tipo de VCS es Git?**
* **Respuesta:** **c) Distribuido**
* **Explicación:** Cada desarrollador cuenta con una copia completa del repositorio y de su historial en su equipo local, lo que permite trabajar sin depender de una conexión constante con un servidor central.

**3. ¿Quién creó Git y en qué año?**
* **Respuesta:** **b) Linus Torvalds, 2005**
* **Explicación:** Linus Torvalds desarrolló Git en 2005 para gestionar de manera eficiente el código fuente del kernel de Linux.

**4. ¿Qué hace `git fetch`?**
* **Respuesta:** **c) Descarga sin fusionar**
* **Explicación:** `git fetch` trae los commits, ramas y referencias nuevas desde el repositorio remoto a tu copia local, pero no mezcla esos cambios automáticamente con tu trabajo actual.

---

## Evaluación: Opción Múltiple (2/2)

**5. Quieres deshacer un commit que ya subiste. ¿Qué usas?**
* **Respuesta:** **b) `git revert`**
* **Explicación:** `git revert` crea un commit nuevo que revierte los cambios del commit anterior, lo cual es seguro en ramas compartidas como `main` porque conserva el historial sin reescribirlo.

**6. ¿Qué es `origin`?**
* **Respuesta:** **c) El nombre por defecto del remoto**
* **Explicación:** Cuando clonas un repositorio o agregas un remoto inicial, Git asigna por defecto el alias `origin` para referirse a la URL del repositorio remoto.

**7. ¿Qué es un fork?**
* **Respuesta:** **a) Una copia del repo en tu cuenta de GitHub**
* **Explicación:** Hacer un fork genera una copia independiente de un repositorio dentro de tu propia cuenta de GitHub para experimentar o proponer cambios mediante un Pull Request.

**8. Los marcadores `<<<<<<<`, `=======`, `>>>>>>>` indican...**
* **Respuesta:** **b) Un conflicto de fusión**
* **Explicación:** Aparecen cuando Git no puede resolver automáticamente dos modificaciones distintas hechas en las mismas líneas durante una fusión (`merge`) o `pull`.

---

## Evaluación: Preguntas Abiertas

### 1. Explica con una analogía propia las tres áreas de Git.
Podemos imaginar el trabajo de un arquitecto al preparar los planos de una obra:

* **Working Directory (Directorio de trabajo):** Es el restirador donde dibujas, borras y haces pruebas libremente sobre los planos actuales sin que exista todavía una versión oficial.
* **Staging Area (Área de preparación):** Es la carpeta de revisión donde colocas únicamente las hojas que ya revisaste y aprobaste para formar parte de la siguiente entrega (`git add`).
* **Repository (Repositorio local):** Es el archivo histórico sellado y fechado donde quedan guardadas las versiones aprobadas (`git commit`), de modo que siempre puedes consultar o recuperar un estado anterior del proyecto.

### 2. ¿Cuándo usarías `git stash`?
Utilizaría `git stash` cuando tengo cambios a medias en mi rama actual (por ejemplo, una función incompleta o pruebas temporales) y necesito cambiar de rama con urgencia o actualizar la rama sin hacer un commit de código sin terminar. Con `git stash` aparto esos cambios de forma temporal y, cuando regreso a mi rama, los recupero con `git stash pop`.

### 3. Encontraste un bug en una librería open source que usa tu sistema. Describe el flujo completo para enviar la corrección.
El flujo habitual para aportar a un repositorio open source donde no tienes acceso directo de escritura es el siguiente:

1. **Hacer un fork:** Creo una copia del repositorio original en mi cuenta de GitHub.
2. **Clonar y configurar remotos:** Clono mi fork a mi computadora (`git clone <url-fork>`) y, si es necesario, agrego el repositorio original como remoto (`git remote add upstream <url-original>`) para mantenerme al día.
3. **Crear una rama de trabajo:** Creo una rama nueva a partir de la rama principal actualizada (por ejemplo, `git switch -c fix/corregir-bug`) para mantener aislado el arreglo.
4. **Aplicar y probar la corrección:** Modifico el código necesario para resolver el problema, verifico con pruebas que todo funcione bien y registro los cambios con `git add` y `git commit`.
5. **Subir la rama a mi fork:** Envío la rama a mi repositorio en GitHub mediante `git push origin fix/corregir-bug`.
6. **Abrir un Pull Request:** Desde GitHub abro un Pull Request desde mi rama hacia la rama principal del proyecto original, explicando claramente el bug encontrado, cómo se reprodujo y cómo se solucionó, para que los mantenedores lo revisen.

### 4. Un compañero subió el `.env` con la contraseña de producción. ¿Por qué es grave y qué pasos sigues?
**Por qué es grave:** El archivo `.env` suele contener secretos sensibles como contraseñas de bases de datos, llaves de API o credenciales de servicios. Una vez que el archivo queda registrado en el historial de Git y se envía a un repositorio remoto, no basta con borrarlo en un commit posterior, ya que sigue existiendo en el historial anterior y puede quedar expuesto ante personas o sistemas automatizados con acceso al repositorio.

**Pasos a seguir:**
1. **Rotar las credenciales de inmediato:** Cambiar de inmediato la contraseña de producción, revocar tokens y generar claves nuevas, dando por hecho que la credencial anterior pudo quedar expuesta.
2. **Dejar de rastrear el archivo sin borrarlo del disco:** Ejecutar `git rm --cached .env` para retirarlo del índice de Git manteniendo la copia local en el equipo.
3. **Añadirlo a `.gitignore`:** Incluir `.env` en `.gitignore` para evitar que vuelva a agregarse por accidente en futuros commits.
4. **Limpiar el historial si corresponde:** Si el repositorio es público o el historial debe sanearse, reescribir el historial con herramientas como `git filter-repo` o BFG Repo-Cleaner y coordinar con el equipo la actualización de sus copias locales.

### 5. Un deploy de ayer rompió producción y el commit ya está en `main`. ¿Usas `reset` o `revert`? ¿Por qué?
Utilizaría **`git revert`**.

Lo hago porque `main` es una rama compartida que ya está desplegada en producción. `git revert` genera un commit nuevo que deshace los cambios del commit problemático sin alterar ni borrar el historial existente, lo que evita desincronizar las copias de otros integrantes del equipo y mantiene un registro claro de qué ocurrió y cómo se corrigió. A diferencia de `git reset --hard`, no reescribe la historia compartida ni exige forzar el envío (`--force`) sobre `main`.

---

## Ejercicio de Diagnóstico

**Secuencia ordenada para publicar un cambio nuevo:**

1. `git switch -c feat/x`
2. `git pull`
3. `editar archivos`
4. `git add .`
5. `git commit -m "..."`
6. `git push`
