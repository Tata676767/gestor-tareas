# Evaluación: Preguntas Abiertas sobre Git y GitHub

## 1. Explica con una analogía propia las tres áreas de Git.
Podemos imaginar el flujo de trabajo como preparar una entrega en un taller:

* **Working Directory (Directorio de trabajo):** Es la mesa donde estás armando y modificando piezas. Puedes probar ideas, rayar o desarmar cosas sin que todavía queden registradas oficialmente.
* **Staging Area (Área de preparación / Index):** Es la caja de envío donde vas metiendo únicamente las piezas que ya revisaste y decidiste que sí van a formar parte de la siguiente entrega (`git add`).
* **Repository (Repositorio local):** Es el almacén sellado y con registro histórico. Una vez que cierras la caja y le pones etiqueta (`git commit`), queda guardada una versión permanente a la que puedes volver en el futuro.

---

## 2. ¿Cuándo usarías `git stash`?
Lo usaría cuando estoy a mitad de un cambio en mi rama actual (con código incompleto o que todavía no compila bien para hacer un commit) y necesito **cambiar de rama urgentemente** para atender otra tarea, como revisar un error o hacer `git pull` sin perder lo que llevo avanzado.

`git stash` guarda temporalmente esas modificaciones en una pila limpia y deja mi directorio de trabajo igual que el último commit; cuando termino la emergencia, regreso a mi rama y recupero mi trabajo con `git stash pop`.

---

## 3. Encontraste un bug en una librería open source que usa tu sistema. Describe el flujo completo para enviar la corrección.
Como no tengo permisos directos de escritura en el repositorio original (*upstream*), sigo el flujo de **Fork & Pull Request**:

1. **Fork:** Hago una copia (fork) del repositorio oficial hacia mi propia cuenta de GitHub.
2. **Clone:** Clono mi fork a mi computadora (`git clone <url-de-mi-fork>`) y agrego el repositorio original como remoto (`git remote add upstream <url-original>`) para mantenerme sincronizado.
3. **Nueva rama:** Creo una rama específica para el arreglo desde `main` actualizada (`git checkout -b fix/nombre-del-bug`), nunca trabajo directo sobre `main`.
4. **Corrección y pruebas:** Corrijo el bug, escribo o corro las pruebas unitarias para asegurar que no rompí nada más y hago commits claros (`git add` y `git commit`).
5. **Push a mi fork:** Subo mi rama a mi repositorio en GitHub (`git push origin fix/nombre-del-bug`).
6. **Pull Request (PR):** Desde GitHub abro un Pull Request apuntando desde mi rama hacia la rama principal del repositorio original, explicando qué causaba el bug y cómo lo solucioné, quedando atento a las revisiones de los mantenedores.

---

## 4. Un compañero subió el `.env` con la contraseña de producción. ¿Por qué es grave y qué pasos sigues?
**¿Por qué es grave?**
Porque el archivo `.env` contiene credenciales críticas (contraseñas de bases de datos, llaves de API, tokens). Una vez que un archivo entra al historial de Git y se sube al remoto, aunque después lo borres en un commit nuevo, **sigue siendo visible en el historial de commits anteriores** para cualquiera que tenga acceso al repositorio (o para bots que escanean repositorios públicos en segundos).

**Pasos a seguir:**
1. **Rotar las credenciales de inmediato (paso más importante):** Cambiar la contraseña de producción, revocar tokens y generar nuevas llaves API. Asumo que la contraseña anterior ya está comprometida.
2. **Eliminar el archivo del seguimiento de Git sin borrarlo localmente:** Ejecutar `git rm --cached .env` para sacarlo del repositorio manteniendo el archivo en la máquina local.
3. **Protegerlo en `.gitignore`:** Agregar `.env` dentro del archivo `.gitignore` para evitar que vuelva a subirse por accidente.
4. **Limpiar el historial de Git (si es necesario):** Usar herramientas como `git filter-repo` o BFG Repo-Cleaner para borrar todo rastro del `.env` en commits pasados y hacer `git push --force`, avisando al equipo para que vuelvan a clonar o sincronizar sus ramas.

---

## 5. Un deploy de ayer rompió producción y el commit ya está en `main`. ¿Usas `reset` o `revert`? ¿Por qué?
Uso **`git revert`**.

**¿Por qué?**
* Porque `main` es una rama compartida y pública que ya está en producción. `git revert <hash-del-commit>` crea un **nuevo commit** que deshace exactamente los cambios del commit defectuoso sin reescribir ni borrar el historial previo.
* Si usara `git reset --hard`, estaría alterando el historial de commits y obligaría a hacer un `git push --force`, lo cual desincronizaría el repositorio de todos mis compañeros y borraría la trazabilidad de lo que ocurrió en producción.
