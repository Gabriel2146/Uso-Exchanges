# Sistema de Notificaciones con RabbitMQ

Este proyecto implementa un sistema de notificaciones utilizando RabbitMQ como gestor de colas. El sistema incluye productores y consumidores que interactúan mediante dos tipos de exchanges: `fanout` y `direct`. Sigue principios de programación modular, estándares en Python y el patrón arquitectónico **Event-Driven Architecture (Broker Pattern)**.

---

## 🛠️ Requisitos Previos

1. **Docker** y **Docker Compose** instalados.
2. **Python 3.8+** y la librería `pika`:
   ```bash
   pip install pika
   ```

---

## 📂 Estructura del Proyecto

```plaintext
queue_system/
├── producers/
│   ├── producer_fanout.py      # Envia mensajes generales
│   ├── producer_direct.py      # Envia mensajes específicos
├── consumers/
│   ├── consumer_general.py     # Recibe notificaciones generales
│   ├── consumer_email.py       # Recibe notificaciones de tipo email
│   ├── consumer_sms.py         # Recibe notificaciones de tipo SMS
├── docker-compose.yml          # Configuración de RabbitMQ
└── README.md                   # Documentación del proyecto
```

---

## 🚀 Configuración y Ejecución

### 1. Levantar RabbitMQ con Docker
Usa el archivo `docker-compose.yml` para iniciar RabbitMQ:

```bash
docker-compose up -d
```

Accede al panel de administración en [http://localhost:15672](http://localhost:15672).  
Credenciales:
- Usuario: `GabrielP`
- Contraseña: `2146`

---

### 2. Ejecutar los Productores y Consumidores

#### Productores
- `producer_fanout.py`: Envia notificaciones generales.
- `producer_direct.py`: Envia notificaciones específicas (email y SMS).

Ejemplo de ejecución:
```bash
python producers/producer_fanout.py
python producers/producer_direct.py
```

#### Consumidores
- `consumer_general.py`: Escucha mensajes del exchange `fanout`.
- `consumer_email.py`: Escucha mensajes etiquetados como `email`.
- `consumer_sms.py`: Escucha mensajes etiquetados como `sms`.

Ejemplo de ejecución:
```bash
python consumers/consumer_general.py
python consumers/consumer_email.py
python consumers/consumer_sms.py
```

---

## 🧩 Patrón Arquitectónico

Este proyecto sigue el patrón **Event-Driven Architecture (Broker Pattern)**:
- **Event Producers**: Los productores generan eventos (notificaciones).
- **Event Broker**: RabbitMQ actúa como un intermediario para distribuir los mensajes.
- **Event Consumers**: Los consumidores procesan los mensajes según sus necesidades.

---

## 📖 Principios Aplicados

1. **SOLID**:
   - Código modular y desacoplado.
   - Responsabilidad única para productores y consumidores.
2. **Buenas Prácticas**:
   - Nombres descriptivos para archivos y funciones.
   - Uso de `virtualenv` para aislar dependencias (opcional).

---

## 🗂️ Repositorio

Este proyecto está disponible en un repositorio público de GitHub. Puedes clonarlo con:
```bash
git clone https://github.com/tuusuario/queue_system.git
```

---

## 🤝 Contribuciones

¡Contribuciones son bienvenidas! Si tienes sugerencias o mejoras, no dudes en hacer un _pull request_.

---

## 📝 Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
