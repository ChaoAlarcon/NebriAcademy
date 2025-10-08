import pandas as pd

# Crear tabla comparativa de plataformas para academias online
plataformas_data = {
    'Plataforma': [
        'LearnDash (WordPress)', 'Moodle', 'Thinkific', 'Teachable', 'Kajabi',
        'Udemy', 'Coursera', 'ClassOnLive', 'LifterLMS', 'TutorLMS'
    ],
    'Tipo': [
        'Plugin LMS', 'LMS Open Source', 'SaaS', 'SaaS', 'SaaS Todo-en-Uno',
        'Marketplace', 'Marketplace Académico', 'Plataforma Española', 'Plugin LMS', 'Plugin LMS'
    ],
    'Precio_desde': [
        '$199/año', 'Gratuito', '$49/mes', '$39/mes', '$149/mes',
        'Gratuito + comisión', 'Gratuito + comisión', '$29/mes', '$99/año', 'Gratuito'
    ],
    'Control_diseño': [
        'Total', 'Total', 'Medio', 'Medio', 'Alto',
        'Limitado', 'Limitado', 'Alto', 'Total', 'Total'
    ],
    'Facilidad_uso': [
        '3/5', '2/5', '5/5', '5/5', '4/5',
        '5/5', '5/5', '4/5', '4/5', '4/5'
    ],
    'Personalización': [
        'Alta', 'Muy Alta', 'Media', 'Media', 'Alta',
        'Baja', 'Baja', 'Alta', 'Alta', 'Alta'
    ],
    'Ideal_para': [
        'Profesionales técnicos', 'Instituciones educativas', 'Emprendedores', 'Creadores de contenido', 'Negocios digitales',
        'Instructores independientes', 'Cursos académicos', 'Academias españolas', 'Pequeñas empresas', 'Principiantes'
    ]
}

df_plataformas = pd.DataFrame(plataformas_data)

print("=== COMPARATIVA DE PLATAFORMAS PARA ACADEMIAS ONLINE ===")
print()

# Mostrar tabla formateada
for i, row in df_plataformas.iterrows():
    print(f"🌐 {row['Plataforma']}")
    print(f"   📁 Tipo: {row['Tipo']}")
    print(f"   💰 Precio: {row['Precio_desde']}")
    print(f"   🎨 Control diseño: {row['Control_diseño']}")
    print(f"   📱 Facilidad uso: {row['Facilidad_uso']}")
    print(f"   ⚙️ Personalización: {row['Personalización']}")
    print(f"   👥 Ideal para: {row['Ideal_para']}")
    print()

# Guardar CSV
df_plataformas.to_csv('comparativa_plataformas_academias.csv', index=False, encoding='utf-8')

print("✅ Comparativa guardada como 'comparativa_plataformas_academias.csv'")
print()

# Crear tabla de tendencias de diseño 2025
tendencias_data = {
    'Tendencia': [
        'Diseño Inclusivo y Accesible',
        'Inteligencia Artificial',
        'Microaprendizaje',
        'Gamificación Avanzada',
        'Realidad Virtual/Aumentada',
        'Diseño Minimalista',
        'Aprendizaje Adaptativo',
        'Contenido Interactivo',
        'Diseño Mobile-First',
        'Comunidades de Aprendizaje'
    ],
    'Descripción': [
        'Cumplimiento WCAG, contraste alto, navegación por teclado',
        'Chatbots, recomendaciones personalizadas, análisis predictivo',
        'Lecciones de 5-10 minutos, contenido consumible',
        'Narrativas inmersivas, recompensas dinámicas, progresión',
        'Experiencias inmersivas para práctica y simulación',
        'Espacios blancos, tipografía clara, elementos esenciales',
        'Rutas de aprendizaje que se ajustan al progreso del usuario',
        'Videos interactivos, simulaciones, ejercicios prácticos',
        'Diseño prioritario para dispositivos móviles',
        'Foros activos, grupos de estudio, peer learning'
    ],
    'Impacto': [
        'Alto', 'Muy Alto', 'Alto', 'Medio', 'Medio',
        'Alto', 'Alto', 'Alto', 'Crítico', 'Alto'
    ],
    'Adopción_2025': [
        '85%', '70%', '90%', '60%', '30%',
        '95%', '45%', '80%', '98%', '75%'
    ]
}

df_tendencias = pd.DataFrame(tendencias_data)

print("\n=== TENDENCIAS DE DISEÑO PARA ACADEMIAS ONLINE 2025 ===")
print()

for i, row in df_tendencias.iterrows():
    impacto_emoji = {
        'Crítico': '🔴',
        'Muy Alto': '🟠',
        'Alto': '🟡',
        'Medio': '🟢'
    }
    print(f"{impacto_emoji[row['Impacto']]} {row['Tendencia']}")
    print(f"   📝 {row['Descripción']}")
    print(f"   📊 Adopción estimada 2025: {row['Adopción_2025']}")
    print()

df_tendencias.to_csv('tendencias_diseno_academias_2025.csv', index=False, encoding='utf-8')
print("✅ Tendencias guardadas como 'tendencias_diseno_academias_2025.csv'")