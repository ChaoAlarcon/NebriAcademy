import pandas as pd

# Crear datos para las mejores prácticas de diseño de academias online
data = {
    'Categoría': [
        'Diseño Visual', 'Diseño Visual', 'Diseño Visual', 'Diseño Visual', 'Diseño Visual',
        'UX/UI', 'UX/UI', 'UX/UI', 'UX/UI', 'UX/UI',
        'Contenido', 'Contenido', 'Contenido', 'Contenido', 'Contenido',
        'Funcionalidad', 'Funcionalidad', 'Funcionalidad', 'Funcionalidad', 'Funcionalidad',
        'Tecnología', 'Tecnología', 'Tecnología', 'Tecnología', 'Tecnología'
    ],
    'Elemento': [
        'Paleta de colores', 'Tipografía', 'Iconografía', 'Imágenes', 'Branding',
        'Navegación intuitiva', 'Diseño responsive', 'Accesibilidad', 'Velocidad de carga', 'Interface limpia',
        'Organización de cursos', 'Dashboard estudiante', 'Progreso visual', 'Biblioteca recursos', 'Contenido multimedia',
        'Sistema LMS', 'Pagos integrados', 'Certificaciones', 'Gamificación', 'Comunicación',
        'Hosting confiable', 'Seguridad de datos', 'Integraciones', 'Backup automático', 'Escalabilidad'
    ],
    'Descripción': [
        'Colores azules/verdes para tranquilidad y confianza', 
        'Fuentes legibles como Open Sans o Nunito',
        'Iconos consistentes y comprensibles',
        'Fotos de alta calidad que inspiren aprendizaje',
        'Identidad visual coherente en toda la plataforma',
        'Máximo 3 clics para llegar a cualquier contenido',
        'Adaptable a móvil, tablet y escritorio',
        'Cumplir estándares WCAG 2.1',
        'Tiempos de carga menores a 3 segundos',
        'Diseño minimalista que no distraiga del contenido',
        'Categorización clara y filtros efectivos',
        'Panel personalizado con progreso y tareas',
        'Barras de progreso y logros visuales',
        'Acceso fácil a materiales complementarios',
        'Videos, audios, PDFs, presentaciones interactivas',
        'Plataforma robusta como Moodle o LearnDash',
        'PayPal, Stripe, pasarelas locales',
        'Certificados descargables y verificables',
        'Puntos, insignias, rankings, desafíos',
        'Foros, chat, mensajería directa',
        'Uptime del 99.9% con soporte 24/7',
        'SSL, encriptación, cumplimiento GDPR',
        'APIs con herramientas de marketing y CRM',
        'Copias de seguridad diarias automáticas',
        'Capacidad de crecimiento sin afectar rendimiento'
    ],
    'Prioridad': [
        'Alta', 'Alta', 'Media', 'Alta', 'Media',
        'Crítica', 'Crítica', 'Alta', 'Crítica', 'Alta',
        'Crítica', 'Alta', 'Media', 'Media', 'Alta',
        'Crítica', 'Alta', 'Media', 'Media', 'Alta',
        'Crítica', 'Crítica', 'Media', 'Alta', 'Media'
    ]
}

df = pd.DataFrame(data)

# Mostrar la tabla
print("=== MEJORES PRÁCTICAS PARA DISEÑO DE ACADEMIAS ONLINE ===")
print()

# Agrupar por categoría para mejor visualización
for categoria in df['Categoría'].unique():
    print(f"📋 {categoria.upper()}")
    print("-" * 50)
    subset = df[df['Categoría'] == categoria]
    
    for _, row in subset.iterrows():
        prioridad_emoji = {
            'Crítica': '🔴',
            'Alta': '🟠', 
            'Media': '🟡'
        }
        print(f"{prioridad_emoji[row['Prioridad']]} {row['Elemento']}")
        print(f"   → {row['Descripción']}")
        print()
    print()

# Guardar como CSV
df.to_csv('mejores_practicas_academias_online.csv', index=False, encoding='utf-8')
print("✅ Tabla guardada como 'mejores_practicas_academias_online.csv'")