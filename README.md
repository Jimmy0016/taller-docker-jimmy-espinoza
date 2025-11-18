# Taller Docker - Jimmy Espinoza

Una aplicación web simple desarrollada con Flask y containerizada con Docker, configurada para despliegue con Docker Swarm y Traefik.

##  Descripción

Esta es una aplicación web básica que muestra un mensaje de saludo personalizado. El proyecto incluye configuración completa para containerización, despliegue automatizado y CI/CD.

##  Características

- Aplicación Flask minimalista
- Containerización con Docker
- Despliegue con Docker Swarm
- Configuración de Traefik para proxy reverso
- CI/CD con GitHub Actions
- Makefile para automatización de tareas

## Tecnologías

- **Python 3.10**
- **Flask 3.1.2**
- **Docker**
- **Docker Swarm**
- **Traefik**
- **GitHub Actions**

##  Estructura del Proyecto

```
taller-docker-jimmy-espinoza/
├── .github/
│   └── workflows/
│       └── publish-docker.yml    # CI/CD pipeline
├── app.py                        # Aplicación Flask
├── Dockerfile                    # Configuración del contenedor
├── requirements.txt              # Dependencias de Python
├── Makefile                      # Comandos automatizados
├── stack.yml                     # Configuración Docker Swarm
├── .dockerignore                 # Archivos ignorados por Docker
└── .gitignore                    # Archivos ignorados por Git
```

## Instalación y Uso

### Prerrequisitos

- Docker
- Docker Compose
- Make (opcional)

### Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone <repository-url>
   cd taller-docker-jimmy-espinoza
   ```

2. **Construir la imagen Docker:**
   ```bash
   docker build -t pgespinoza:1.0.1 .
   ```

3. **Ejecutar el contenedor:**
   ```bash
   docker run -p 8080:80 pgespinoza:1.0.1
   ```

4. **Acceder a la aplicación:**
   Abrir http://localhost:8080 en el navegador

### Usando Makefile

```bash
# Construir la imagen
make build

# Desplegar en Docker Swarm
make deploy

# Ver logs
make logs

# Ver servicios activos
make ps

# Reiniciar completamente
make restart

# Remover el stack
make rm
```

##  Docker

### Dockerfile

La imagen se basa en `python:3.10-slim` e incluye:
- Instalación de dependencias desde `requirements.txt`
- Exposición del puerto 8080
- Comando de inicio automático

### Docker Swarm

El archivo `stack.yml` configura:
- 1 réplica del servicio
- Integración con Traefik para proxy reverso
- Configuración SSL automática
- Red externa `traefik-public`

##  Despliegue

### Configuración de Traefik

El servicio está configurado para:
- **Dominio:** `pgespinoza.byronrm.com`
- **Redirección HTTPS automática**
- **Certificados SSL automáticos**
- **Puerto interno:** 80

### CI/CD

GitHub Actions automatiza:
- Construcción de la imagen Docker
- Publicación en registry
- Despliegue automático

##  API Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/`      | GET    | Mensaje de saludo |

##  Configuración

### Variables de Entorno

- `PORT`: Puerto de la aplicación (default: 8080)

### Dependencias

Ver `requirements.txt` para la lista completa de dependencias de Python.

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

##  Licencia

Este proyecto es parte de un taller educativo sobre Docker.

##  Autor

**Jimmy Espinoza**

---

Si este proyecto te fue útil, ¡no olvides darle una estrella!