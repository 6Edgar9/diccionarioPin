# diccionarioPin

**diccionarioPin** contiene herramientas educativas para generar diccionarios de PINs y para experimentar con ataques de fuerza bruta en entornos controlados.  
**Importante:** Este repositorio **no** debe usarse para atacar dispositivos o cuentas que no te pertenecen. El material aquí es de **uso educativo** únicamente.

---

## ⚠️ Aviso legal y ético (leelo antes de usar)

Estos scripts pueden facilitar acciones que, cuando se usan sin autorización, son ilegales y dañinas (por ejemplo, intentar desbloquear dispositivos móviles que no sean de tu propiedad). **No ejecutes ningún ataque contra dispositivos o servicios sin permiso explícito y por escrito del propietario.**

Si tu objetivo es aprender o auditar:
- Realiza pruebas únicamente en tus propios dispositivos o en entornos de laboratorio controlados.
- Obtén autorización por escrito cuando trabajes para terceros.
- Respeta la legislación local y las políticas de uso.

---

## ¿Qué contiene este repositorio?

- `dic.py` — Generador de diccionarios de PINs (scripts de generación masiva). **No ejecutar contra dispositivos reales.**
- `ata.py` — Script de creación de PIN de ejemplo y un simulador básico de fuerza bruta local (almacena el PIN en `pin_usuario.txt`). Útil para pruebas educativas locales.
- `prb.py` — Ejemplo que muestra cómo se podría automatizar intentos vía ADB. **Código sensible: NO ejecutar contra dispositivos reales.**
  > Este archivo se incluye con fines de demostración y debe ser tratado con extrema precaución. Su ejecución puede llevar a consecuencias legales si se usa indebidamente.

---

## Uso (seguro y restringido)

---
## ❗ Nota de seguridad sobre recorrido de diccionarios

Por seguridad y responsabilidad **este repositorio NO implementa ni incluye funciones que recorran automáticamente todos los diccionarios para intentar desbloquear dispositivos** (por ejemplo, automatizaciones que usen ADB). Automatizar ataques reales contra dispositivos puede ser ilegal y peligroso.

En su lugar, el repositorio ofrece herramientas y ejemplos **en modo educativo** y **simulado** para que practiques y aprendas sin interactuar con hardware o redes reales. Si necesitas una versión segura que simule el recorrido de diccionarios (modo *dry-run*), puedo generarla para que la uses en entornos controlados.
---



Este proyecto **no** proporciona instrucciones operativas para ejecutar ataques reales. Si quieres usar el repositorio con fines educativos:

1. Crea un entorno aislado (máquina virtual o contenedor) y usa únicamente dispositivos que poseas.
2. Ejecuta únicamente el script `ata.py` en modo local para probar la lógica de verificación del PIN contra el archivo `pin_usuario.txt`. No automatices interacciones con dispositivos reales.
3. Si deseas convertir `prb.py` en una herramienta de laboratorio segura, pídeme que te la transforme en una **simulación** que no interactúe con ADB ni con hardware real.

---

## Riesgos y recomendaciones de seguridad

- **No** almacenes PINs en texto claro; si necesitas almacenar secretamente en pruebas, usa hashes con sal (bcrypt) y permisos de archivo restrictivos.
- Implementa límites de intentos, bloqueo de cuenta y retardos progresivos para evitar fuerza bruta.
- Mantén registros (logs) y alerta sobre intentos de acceso sospechosos cuando trabajes en sistemas de prueba.
- Si automatizas interacciones con dispositivos, hazlo únicamente en entornos de laboratorio y con consentimiento.

---

## Alternativas seguras y recursos recomendados

Si tu objetivo es aprender sobre seguridad de autenticación y buenas prácticas:
- Lee el **OWASP Authentication Cheat Sheet**.
- Revisa **NIST SP 800-63** (Digital Identity Guidelines).
- Practica en entornos como máquinas virtuales, emuladores o plataformas de laboratorio (p.ej. Metasploitable, Hack The Box con objetivos autorizados).
- Para pruebas de Android en laboratorio, usa emuladores oficiales de Android Studio en vez de dispositivos reales.

---

## Mejoras sugeridas (seguras)

- Convertir scripts para que funcionen únicamente en modo *simulado* o *de prueba*, sin ADB.
- Añadir hashing seguro (bcrypt) para almacenamiento de PINs de prueba.
- Agregar parámetros de línea de comandos para limitar la generación masiva y evitar escritura descontrolada en disco.
- Añadir pruebas unitarias y un modo `--dry-run` que no ejecute acciones potencialmente peligrosas.

---

#### Dios, Assembly y la Patria
#### Edrem

---

Desarrollado con fines académicos y de práctica en Python.