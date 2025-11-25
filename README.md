# Taller Docker - Jimmy Espinoza

Una aplicación web Flask con IA integrada, containerizada con Docker y configurada para CI/CD completo con GitHub Actions y despliegue automático.

## 🚀 Descripción

Aplicación Flask con funcionalidad de IA simulada que demuestra un pipeline completo de CI/CD, incluyendo:
- Tests automatizados
- Construcción y publicación de imágenes en GitHub Container Registry (GHCR)
- Despliegue automático en VPS con Docker Swarm
- Configuración de Traefik para proxy reverso y SSL

## ✨ Características

- **Aplicación Flask con IA**: Endpoints que simulan respuestas de inteligencia artificial
- **Tests automatizados**: Suite completa de pruebas con pytest
- **CI/CD Pipeline**: GitHub Actions para integración y despliegue continuo
- **Containerización**: Docker optimizado con mejores prácticas
- **Despliegue automático**: Docker Swarm con Traefik
- **SSL automático**: Certificados Let's Encrypt via Traefik

## 🛠 Tecnologías

- **Python 3.10**
- **Flask 3.1.2**
- **Docker & Docker Swarm**
- **GitHub Container Registry (GHCR)**
- **GitHub Actions**
- **Traefik**
- **pytest**

## 📁 Estructura del Proyecto

```
taller-docker-jimmy-espinoza/
├── .github/
│   └── workflows/
│       └── deployfinal.yml      # Pipeline CI/CD
├── app.py                       # Aplicación Flask con IA
├── test_app.py                  # Tests automatizados
├── Dockerfile                   # Configuración optimizada del contenedor
├── requirements.txt             # Dependencias Python + testing
├── Makefile                     # Comandos automatizados
├── stack.yml                    # Configuración Docker Swarm
├── pytest.ini                  # Configuración de tests
├── .dockerignore               # Archivos ignorados por Docker
└── README.md                   # Documentación
```

## 🌐 Endpoints de la API

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/`      | GET    | Página principal con información |
| `/ai`    | GET    | Consulta a la IA simulada |
| `/health`| GET    | Estado de salud de la aplicación |
| `/info`  | GET    | Información del sistema |

## 🚀 Instalación y Uso

### Prerrequisitos

- Docker
- Make (opcional)
- Python 3.10+ (para desarrollo local)

### Desarrollo Local

1. **Clonar el repositorio:**
   ```bash
   git clone <repository-url>
   cd taller-docker-jimmy-espinoza
   git checkout espinoza
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar tests:**
   ```bash
   make test
   # o
   python -m pytest test_app.py -v
   ```

4. **Construir y ejecutar con Docker:**
   ```bash
   make build
   make run
   # o
   docker build -t ghcr.io/jimmy0016/espinoza:1.0.5 .
   docker run -p 8080:80 ghcr.io/jimmy0016/espinoza:1.0.5
   ```

5. **Acceder a la aplicación:**
   - Local: http://localhost:8080
   - Producción: https://espinoza.byronrm.com

### Comandos Make Disponibles

```bash
make test      # Ejecutar tests
make build     # Construir imagen Docker
make run       # Ejecutar contenedor localmente
make deploy    # Desplegar en Docker Swarm
make logs      # Ver logs del servicio
make ps        # Ver servicios activos
make restart   # Reiniciar completamente
make rm        # Remover stack
```

## 🔄 CI/CD Pipeline

### Flujo Automatizado

1. **Push a rama `espinoza`** → Trigger del pipeline
2. **Tests**: Ejecución de pytest
3. **Build**: Construcción de imagen Docker
4. **Publish**: Publicación en GHCR como `ghcr.io/jimmy0016/espinoza:1.0.5`
5. **Deploy**: Despliegue automático en VPS

### Configuración del Pipeline

- **Tests**: pytest con cobertura completa
- **Registry**: GitHub Container Registry (GHCR)
- **Imagen**: `ghcr.io/jimmy0016/espinoza:1.0.5`
- **Despliegue**: Docker Swarm automático
- **SSL**: Certificados automáticos via Traefik

## 🐳 Docker

### Imagen Optimizada

- Base: `python:3.10-slim`
- Usuario no-root para seguridad
- Cache optimizado de dependencias
- Tamaño mínimo de imagen

### Docker Swarm

Configuración en `stack.yml`:
- 1 réplica del servicio
- Integración completa con Traefik
- Red `traefik-public`
- SSL automático

## 🌍 Despliegue en Producción

### Dominio y SSL

- **URL**: https://espinoza.byronrm.com
- **SSL**: Certificados automáticos Let's Encrypt
- **Proxy**: Traefik con redirección HTTPS

### Monitoreo

```bash
# Ver servicios
docker service ls

# Ver logs en tiempo real
docker service logs -f espinoza-stack_espinoza-app

# Estado de contenedores
docker ps
```

## 🧪 Testing

### Suite de Pruebas

- Tests de endpoints principales
- Validación de respuestas JSON
- Verificación de códigos de estado
- Tests de funcionalidad de IA

### Ejecutar Tests

```bash
# Con make
make test

# Directamente con pytest
python -m pytest test_app.py -v

# Con cobertura
python -m pytest test_app.py --cov=app
```

## 📊 Versioning

- **Versión actual**: 1.0.5
- **Rama de desarrollo**: espinoza
- **Registry**: GitHub Container Registry (GHCR)

## 🤝 Contribución

1. Fork el proyecto
2. Crear rama desde `espinoza`
3. Realizar cambios y tests
4. Push activará CI/CD automático
5. Verificar despliegue en https://espinoza.byronrm.com

## 📝 Licencia

Proyecto educativo para examen de CI/CD - Jimmy Espinoza

## 👨‍💻 Autor

**Jimmy Espinoza**
- Proyecto: Examen CI/CD
- Rama: espinoza
- Dominio: espinoza.byronrm.com

---

🌟 **Pipeline Status**: [![CI/CD](https://github.com/jimmy0016/taller-docker-jimmy-espinoza/actions/workflows/deployfinal.yml/badge.svg?branch=espinoza)](https://github.com/jimmy0016/taller-docker-jimmy-espinoza/actions/workflows/deployfinal.yml)

🚀 **Live Demo**: [https://espinoza.byronrm.com](https://espinoza.byronrm.com)