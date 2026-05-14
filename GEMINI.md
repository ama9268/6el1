# 6el1 Digital Solutions - Project Architecture & Design

## 🚀 Visión del Proyecto
6el1 Digital Solutions es un SaaS de consultoría estratégica y soluciones digitales de alta gama. El objetivo es ofrecer una experiencia de usuario premium que refleje precisión técnica, innovación en IA y minimalismo atmosférico.

## 🏗️ Arquitectura Técnica
- **Framework**: Django 5.1.7 (Python 3.13.6)
- **Styling**: Tailwind CSS (via `django-tailwind`)
- **Base de Datos**: PostgreSQL (Externa)
- **Patrones de Diseño**: 
  - **Vistas Basadas en Clases (CBV)** para toda la lógica de presentación.
  - **Mixins** para gestión de permisos y estados.
  - **Context Processors** para datos globales (branding, configuración).

## 🎨 Sistema de Diseño (Digital Ethereal)
Basado en el proyecto de Stitch:
- **Estética**: Minimalismo Técnico / Atmosférico.
- **Colores Primarios**: 
  - Electric Blue: `#0052ff`
  - Digital White: `#F8FAFC`
  - Soft Slate: `#64748b`
- **Tipografía**:
  - Headings: **Geist** (Precisión técnica).
  - Body: **Inter** (Legibilidad máxima).
- **Componentes**: Bordes redondeados de 8px (0.5rem), sombras ambientales suaves.

## 📂 Estructura de Aplicaciones
- `core/`: Contenido público, landing pages, contacto.
- `dashboard/`: Zona privada para clientes y administración.
- `theme/`: Aplicación dedicada a Tailwind CSS.
- `config/`: Configuración central del proyecto.

## 🛠️ Skills Integradas
- `frontend-design`: Excelencia visual y componentes premium.
- `seo-audit`: Optimización para buscadores en la parte pública.
- `ux-persuasion-engineer`: Estrategias de conversión para el SaaS.
- `api-patterns`: Estructura limpia para futuras integraciones.
