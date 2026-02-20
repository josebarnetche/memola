---
name: MEMOLA Sales
slug: memola-sales
description: Sales and quoting system for Memola Medios S.A.S. — Project-based services for NEA Argentina businesses
category: sales
complexity: complex
version: "2.0.0"
author: "Memola Medios S.A.S."
triggers:
  - "sell"
  - "pitch"
  - "sales"
  - "outreach"
  - "prospect"
  - "email campaign"
  - "send email"
  - "follow up"
  - "close deal"
  - "pitch memola"
  - "pitch jose"
  - "brevo"
  - "quote"
  - "proposal"
  - "presupuesto"
tags:
  - sales
  - outreach
  - email
  - brevo
  - automation
  - nea-argentina
  - prospecting
dependencies:
  skills:
    - memola
examples_dir: "./templates"
---

# MEMOLA Sales — Sistema de Ventas por Proyecto

Sistema de prospección, pitch y cierre para José Barnetche y Memola Medios S.A.S.
Modelo basado en proyectos con entregables claros y precios reales.

---

## 0. VIGIL Integration — Qualification Required

**This skill integrates with MEMOLA's VIGIL agent for prospect qualification.**

### Dependency
```
npx skills add https://github.com/josebarnetche/memola --skill MEMOLA
```

### VIGIL Protocol — Before Any Outreach

1. **Run terrain assessment** — Score prospect on 5 foundation questions
2. **Check Big Agro criteria** — Sector, facturación, NEA presence
3. **Score qualification** — Only proceed if 4/5 or higher
4. **Document decision** — Log in prospect-tracker.json

### Priority Sectors (VIGIL Filter)

| Tier | Sectors | Ticket Potential |
|------|---------|------------------|
| **A** | Frigoríficos, Cabañas genética, Consignatarias grandes, Cooperativas | AR$ 2-7M |
| **B** | Estancias, Agroinsumos, Acopios, Consignatarias medianas | AR$ 800K-2M |
| **C** | Veterinarias rurales, Transportistas, Proveedores | AR$ 500K-800K |

### Qualification Triggers

| Trigger | Action |
|---------|--------|
| `vigil qualify [prospect]` | Run full qualification |
| `vigil sweep` | Scan network for Big Agro opportunities |
| `vigil filter agro` | List qualified Big Agro prospects |

**See:** `templates/vigil-client-filter.md` for full qualification protocol

---

## 1. Quiénes Somos

### José Barnetche
- **Posición:** Fundador de Memola Medios S.A.S., Mercedes, Corrientes
- **Diferencial:** Único fundador operando desde el interior (no Buenos Aires)
- **Background:** AI + industrias tradicionales, full-stack (producción, código, estrategia, música)
- **Red:** Conoce 4000+ personas locales, trabajó con 100+
- **Familia:** Cuarta generación vasco-argentina, familia fundadora Sociedad Rural (1900)

### Memola Medios S.A.S.
- **No es:** Una agencia de marketing con retainers inflados
- **Es:** Operador estratégico que entrega proyectos concretos
- **Base:** Mercedes, Corrientes — NEA Argentina
- **Ventaja:** Origen provincial = conocimiento profundo del NEA, red cálida, confianza local
- **Razón Social:** Memola Medios S.A.S. — Sociedad por Acciones Simplificada

---

## 2. Service Ladder — Escalera de Servicios

```
┌─────────────────────────────────────────────────────────────────┐
│  LEVEL 4: PRODUCCIÓN AUDIOVISUAL                               │
│  Video institucional, tutoriales, cobertura eventos            │
│  AR$ 800.000 - 7.500.000 + IVA                                 │
├─────────────────────────────────────────────────────────────────┤
│  LEVEL 3: AMPLIFICACIÓN                                        │
│  Meta Ads + Email Marketing campaigns                          │
│  AR$ 600.000 - 4.250.000 + IVA                                 │
├─────────────────────────────────────────────────────────────────┤
│  LEVEL 2: OPTIMIZACIÓN                                         │
│  Diseño/Branding + Funnel optimization                         │
│  AR$ 150.000 - 1.500.000 + IVA                                 │
├─────────────────────────────────────────────────────────────────┤
│  LEVEL 1: FUNDACIÓN                                            │
│  Website (+ email incl.) + Analytics tracking                  │
│  AR$ 500.000 - 1.500.000 + IVA                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Todos los precios:** + IVA
**Agendar consultoría:** https://tidycal.com/memola/consultoria

---

## 3. LEVEL 1: FUNDACIÓN — Presencia Digital Básica

Entry point para clientes sin presencia digital profesional.

### 3.1 Website / Rediseño Web

| Tipo | Precio | Incluye |
|------|--------|---------|
| One-page (5-7 secciones) | AR$ 500.000 + IVA | Responsive, form, copy básico |
| Multi-page (hasta 5 páginas) | AR$ 800.000 - 1.200.000 + IVA | + Navegación, más contenido |
| E-commerce básico | AR$ 1.500.000+ + IVA | + Carrito, pagos, catálogo |

**Email corporativo incluido:** Hasta 10 casillas (@empresa.com.ar) en todos los planes web.

**Delivery:** 2-4 semanas
**Payment:** 30% seña / 70% al finalizar

### 3.2 Analytics Tracking

**Scope:** Google Analytics 4 setup completo

| Servicio | Precio |
|----------|--------|
| GA4 setup básico | AR$ 200.000 + IVA |
| GA4 + eventos + conversiones | AR$ 300.000 + IVA |
| Setup completo + dashboard | AR$ 400.000 + IVA |

**Incluye:**
- GA4 property creation
- Event configuration
- Conversion tracking
- Basic dashboard/reporting

**Delivery:** 1 semana
**Note:** Puede venderse standalone o bundled con web

### 3.3 Bundle: Fundación Completa

- Website (one-page) + Email corporativo + Analytics
- **AR$ 650.000 + IVA** (vs AR$ 700.000+ separado)

---

## 4. LEVEL 2: OPTIMIZACIÓN — Crecimiento Estructurado

Para clientes con presencia básica que necesitan convertir mejor.

### 4.1 Diseño / Branding

| Servicio | Precio |
|----------|--------|
| Logo + manual de marca básico | AR$ 400.000 - 600.000 + IVA |
| Rebranding completo | AR$ 800.000 - 1.500.000 + IVA |
| Piezas gráficas (pack 10) | AR$ 250.000 + IVA |

**Delivery:** 2-4 semanas

### 4.2 Funnel Optimization

| Servicio | Precio |
|----------|--------|
| Landing page adicional | AR$ 300.000 - 500.000 + IVA |
| A/B testing setup | AR$ 200.000 + IVA |
| Form optimization + lead capture | AR$ 150.000 + IVA |
| Full funnel audit + recommendations | AR$ 400.000 + IVA |

**Delivery:** 1-2 semanas por landing

---

## 5. LEVEL 3: AMPLIFICACIÓN — Escala Paga

Para clientes listos para invertir en adquisición paga.

### 5.1 Meta Ads (Facebook/Instagram)

| Servicio | Precio | Tipo |
|----------|--------|------|
| Setup inicial (cuenta, píxel, 4 campañas) | AR$ 1.210.000 IVA incl. | One-time |
| Optimización mensual | AR$ 300.000 - 500.000 + IVA/mes | Opcional, recurrente |

**Campañas incluidas en setup:**
1. Alcance
2. Recordación de marca
3. Agregado de carritos
4. Ventas

**Presupuesto publicitario recomendado:** AR$ 1.500.000+/mes (paga cliente directo a Meta)

**Delivery:** 1 semana setup
**Referencia:** Propuesta Mi Ajuar

### 5.2 Email Marketing Campaigns

| Servicio | Precio |
|----------|--------|
| Pack de plantillas (8 templates) | AR$ 600.000 + IVA |
| 16 diseños únicos (2 por plantilla) | AR$ 1.000.000 + IVA |
| Automation básica (welcome + abandoned cart) | AR$ 400.000 + IVA |
| Full package (4 landings + 8 plantillas + 16 diseños + Analytics) | AR$ 4.250.000 + IVA |

**Automation incluida en Full package:**
- Welcome sequence (3 emails)
- Abandoned cart recovery (2 emails)
- Post-purchase follow-up (2 emails)

**Delivery:** 2-3 semanas

### 5.3 Bundle: Ads + Email Package

- Meta Ads setup + Email templates (8)
- **AR$ 1.600.000 + IVA** (vs AR$ 1.810.000 separado)

---

## 6. LEVEL 4: PRODUCCIÓN AUDIOVISUAL — Contenido Premium

Servicios de producción de alto valor.

### 6.1 Video Institucional

**Scope:** Video corporativo/marca

| Duración | Precio |
|----------|--------|
| Hasta 2 minutos | AR$ 1.500.000 - 2.500.000 + IVA |
| 3-5 minutos | AR$ 2.500.000 - 4.000.000 + IVA |

**Incluye:** Pre-producción, filmación (Sony FX3), edición profesional

**Delivery:** 3-5 semanas

### 6.2 Video Tutoriales / Capacitación

**Scope:** Videos técnicos/formativos

| Servicio | Precio |
|----------|--------|
| Video tutorial (<5 min) | AR$ 2.950.000 + IVA |
| Pack de 3 tutoriales | AR$ 7.500.000 + IVA |

**Incluye:** Screen capture integration, audio profesional (DJI Mic 2)

**Viáticos adicionales:**
| Destino | Precio |
|---------|--------|
| Mercedes | AR$ 48.000 + IVA |
| Regional (hasta 300km) | AR$ 278.000 + IVA |
| Nacional | AR$ 412.000+ + IVA |

**Delivery:** 2-4 semanas por video
**Referencia:** Propuesta Agronorte

### 6.3 Cobertura de Eventos

| Servicio | Precio |
|----------|--------|
| Medio día (4hs) | AR$ 800.000 + IVA |
| Día completo | AR$ 1.200.000 + IVA |

**Incluye:** Highlights video, fotos editadas

### 6.4 Fotografía Profesional

| Servicio | Precio |
|----------|--------|
| Sesión producto (10 fotos) | AR$ 300.000 + IVA |
| Sesión corporativa (20 fotos) | AR$ 500.000 + IVA |
| Sesión completa (50+ fotos) | AR$ 800.000 + IVA |

---

## 7. Customer Journey Map

```
PROSPECT
    │
    ▼
[Discovery Call] ─── tidycal.com/memola/consultoria
    │
    ▼
LEVEL 1: ¿Tiene presencia digital básica?
    │
    ├─ NO → Website + Email + Analytics (Bundle Fundación)
    │
    └─ SÍ → Auditoría rápida
              │
              ▼
LEVEL 2: ¿Convierte bien? ¿Tiene marca clara?
    │
    ├─ NO → Branding / Funnel optimization / Landing pages
    │
    └─ SÍ →
              │
              ▼
LEVEL 3: ¿Está listo para escalar con pauta?
    │
    ├─ SÍ → Meta Ads + Email Marketing
    │        (+ optimización mensual opcional)
    │
    └─ WAIT → Nurture until ready
              │
              ▼
LEVEL 4: ¿Necesita contenido premium?
    │
    └─ Video institucional / Tutoriales / Cobertura eventos
```

---

## 8. Upsell Triggers

| Servicio Actual | Upsell Natural | Señal de Trigger |
|-----------------|----------------|------------------|
| Website | Analytics | "¿Cómo mido si funciona?" |
| Analytics | Funnel Opt | Bounce rate >60%, pocos leads |
| Website | Branding | "Mi logo es viejo" / inconsistencia visual |
| Funnel | Meta Ads | Conversión OK, necesita más tráfico |
| Meta Ads | Optimización mensual | "No tengo tiempo para manejar esto" |
| Meta Ads | Email Marketing | Base de leads creciendo |
| Any | Audiovisual | Evento, rebrand, nuevo producto, aniversario |

---

## 9. Payment Terms

| Monto del Proyecto | Estructura de Pago |
|--------------------|-------------------|
| < AR$ 500.000 | 100% upfront |
| AR$ 500.000 - 2.000.000 | 30% seña / 70% al finalizar |
| > AR$ 2.000.000 | 30% / 40% / 30% (milestones) |
| Servicios mensuales | Facturación mensual anticipada |

---

## 10. Framework de Calificación

### Las Cinco Preguntas Diagnósticas

Antes de hacer pitch, evaluar fit:

1. **¿Puede sobrevivir el tiempo suficiente para que la estructura importe?**
   - Si vida útil < 3 años → solo Level 1

2. **¿El fracaso aquí es erosión, no explosión?**
   - Erosión = terreno MEMOLA
   - Ruptura = no es terreno MEMOLA

3. **¿La legitimidad es más valiosa que la velocidad?**
   - Si ser primero importa más que ser confiable → declinar

4. **¿La claridad realmente cambiará los resultados?**
   - Si la estrategia es irrelevante para la supervivencia → no forzar

5. **¿Esto funciona sin volverse viral?**
   - Si la viralidad es requisito → MEMOLA es la herramienta incorrecta

**Scoring:** 4-5 "sí" = proceder. 2-3 = precaución. 0-1 = declinar.

---

## 11. Integración Brevo Email

### Configuración

Set environment variable:
```bash
export BREVO_API_KEY="your-api-key-here"
```

```python
import os
BREVO_API_KEY = os.environ.get("BREVO_API_KEY")
FROM_EMAIL = "agencia@memola.media"
FROM_NAME = "Memola Medios S.A.S."
API_ENDPOINT = "https://api.brevo.com/v3/smtp/email"
```

### Estructura del Payload
```json
{
  "sender": {
    "name": "Memola Medios S.A.S.",
    "email": "agencia@memola.media"
  },
  "to": [{"email": "prospect@company.com"}],
  "subject": "Asunto",
  "textContent": "Cuerpo del email",
  "tags": ["Campaña", "Ciudad", "Sector"]
}
```

---

## 12. Templates de Email

### Email de Descubrimiento (Outreach Frío)

**Asunto:** ¿{company} ya tiene presencia digital profesional?

```
Hola,

Soy José de Memola Medios. Trabajamos con empresas del NEA que están profesionalizando su presencia digital.

Notamos que {company} podría beneficiarse de:

• Sitio web profesional con captura de leads
• Email corporativo (@empresa.com.ar)
• {discovery_question}

Tenemos un paquete de entrada desde AR$ 500.000 + IVA que incluye web + email corporativo.

¿Le interesa una consultoría de 15 minutos?

Agendar: https://tidycal.com/memola/consultoria

Saludos desde Mercedes,

José Barnetche
Memola Medios S.A.S.
agencia@memola.media
```

### Email de Seguimiento (Día 7)

**Asunto:** Seguimiento: Presencia Digital para {company}

```
Hola,

Hace unos días le escribí sobre la presencia digital de {company}.

Quería compartir nuestra oferta de entrada:

BUNDLE FUNDACIÓN — AR$ 650.000 + IVA
• Sitio web one-page responsive
• Email corporativo (hasta 10 casillas)
• Google Analytics configurado

Delivery: 2-4 semanas
Pago: 30% seña / 70% al finalizar

¿Le interesa una consultoría de 15 minutos?

Agendar: https://tidycal.com/memola/consultoria

O puede escribirme directo:
WhatsApp: +54 9 3773 418130

Saludos,
José Barnetche
Memola Medios S.A.S.
```

### Email Post-Proyecto (Upsell)

**Asunto:** {company}: Siguiente paso para crecer

```
Hola,

Completamos {project_delivered} hace {weeks} semanas.

Basado en los resultados, creo que {company} está listo para el siguiente nivel:

{upsell_recommendation}

¿Tiene 15 minutos esta semana para conversarlo?

Agendar: https://tidycal.com/memola/consultoria

Saludos,
José
```

---

## 13. Manejo de Objeciones

### "Es muy caro"
**Respuesta:** "Entiendo. Permítame ponerlo en perspectiva: un desarrollador freelance en Buenos Aires cobra AR$ 800.000-1.500.000 por un sitio similar, sin incluir el diseño ni el seguimiento. Nosotros entregamos todo llave en mano. ¿Qué presupuesto tenía en mente?"

### "No necesitamos presencia digital"
**Respuesta:** "Respeto esa posición. Pregunta sincera: ¿sus clientes actuales los buscan en Google antes de contactarlos? ¿Sus competidores tienen presencia online? Si la respuesta es sí a cualquiera, la ausencia digital es un costo invisible que están pagando."

### "Ya tenemos alguien que maneja eso"
**Respuesta:** "Perfecto. ¿Están contentos con los resultados? Si hay algún área donde sienten que podrían mejorar, podríamos complementar sin reemplazar. ¿Qué aspectos les gustaría fortalecer?"

### "No tenemos tiempo para esto"
**Respuesta:** "Justamente eso resolvemos. Nosotros nos encargamos de todo — ustedes solo aprueban. El compromiso de tiempo es una reunión inicial y feedback sobre borradores. ¿Eso es manejable?"

### "Déjeme pensarlo"
**Respuesta:** "Por supuesto. Para ayudarle a decidir, ¿qué información adicional necesitaría? También puede agendar cuando quiera: https://tidycal.com/memola/consultoria"

---

## 14. Pipeline de Prospectos

### Fuentes de Datos
- `prospect-tracker.json` — Prospectos activos con estado
- `HEARTBEAT.md` — Clientes activos y pipeline
- `.agents/memory/` — Contexto profundo sobre José y MEMOLA

### Estados de Prospectos
1. **New** — Recién identificado, sin contacto
2. **Initial Sent** — Email de descubrimiento enviado
3. **Follow-up Sent** — Email de seguimiento enviado
4. **Response Received** — Prospecto respondió
5. **Meeting Scheduled** — Llamada/reunión agendada
6. **Proposal Sent** — Propuesta formal entregada
7. **Closed Won** — Deal cerrado
8. **Closed Lost** — Declinó o sin respuesta

---

## 15. Workflows

### Workflow 0: VIGIL Qualification (REQUIRED FIRST)
```
1. Identify prospect source (network, referral, research)
2. Run VIGIL terrain assessment:
   a. Score 5 foundation questions (SÍ/NO)
   b. Check Big Agro checklist (must-haves)
   c. Count bonus points
   d. Check red flags
3. Calculate qualification score:
   - 4-5/5 = PROCEED
   - 3/5 = CAUTION (Level 1 only)
   - 0-2/5 = DECLINE
4. If PROCEED:
   a. Log to prospect-tracker.json
   b. Assign tier (A/B/C)
   c. Continue to Outreach workflow
5. If DECLINE:
   a. Log reason
   b. Do NOT pursue
```

### Workflow: Campaña de Outreach Frío (Big Agro)
```
1. Run VIGIL sweep for Big Agro sectors
2. Filter: qualified prospects only (score >= 4/5)
3. Prioritize by tier: A > B > C
4. For each qualified prospect:
   a. Read sector context from vigil-client-filter.md
   b. Craft personalized discovery email
   c. Send via Brevo API
   d. Update status to "Initial Sent"
   e. Log qualification score
5. Report: sent count, tier breakdown, declined count
```

### Workflow: Discovery → Proposal
```
1. Recibir contexto del prospecto
2. Correr cinco preguntas diagnósticas
3. Identificar nivel de servicio apropiado (1-4)
4. Si Level 1:
   a. Ofrecer Bundle Fundación o componentes
5. Si Level 2-3:
   a. Identificar servicios específicos necesarios
   b. Calcular precio total
6. Si Level 4:
   a. Definir scope de producción
   b. Incluir viáticos si aplica
7. Generar propuesta con payment terms
8. Incluir CTA de Tidycal
```

### Workflow: Post-Project Upsell
```
1. Identificar proyecto completado hace 2-4 semanas
2. Revisar upsell triggers
3. Si hay señal de trigger:
   a. Identificar servicio del siguiente nivel
   b. Preparar pitch específico
   c. Enviar email de upsell
4. Si no hay señal:
   a. Agendar check-in para próximo mes
```

---

## 16. Voz de José

### Tono
- **Directo:** Sin florituras corporativas, decir lo que se quiere decir
- **Confiado:** Conocer el valor, no disculparse por precios
- **Local:** Usar "NEA", referenciar especificidades regionales
- **Confianza humilde:** No arrogante, pero seguro

### Patrones de Lenguaje
- "Trabajamos con empresas que entienden que..."
- "En nuestra experiencia con clientes similares..."
- "No vendemos horas. Entregamos proyectos."
- "Desde Mercedes para toda la región NEA."

### Evitar
- Prometer de más ("resultados garantizados")
- Lenguaje desesperado ("por favor considere")
- Jerga genérica de marketing ("sinergia", "leverage")
- Framing porteño-céntrico
- Mencionar retainers mensuales (modelo viejo)

---

## 17. Referencia Rápida

| Acción | Trigger |
|--------|---------|
| Enviar outreach frío | "send discovery email to [prospect]" |
| Enviar seguimiento | "send follow-up to [prospect]" |
| Cotizar proyecto | "quote [service] for [prospect]" |
| Calificar prospecto | "qualify [prospect]" |
| Ver pipeline | "show prospect pipeline" |
| Redactar propuesta | "draft proposal for [prospect]" |
| Manejar objeción | "objection: [texto objeción]" |
| Upsell check | "check upsell for [client]" |

---

## 18. Lineamientos Éticos

1. **Nunca spam** — Máximo 3 contactos por prospecto
2. **Respetar "no"** — Remover del pipeline inmediatamente
3. **Posicionamiento honesto** — No sobrevender capacidades
4. **Privacidad** — No compartir datos de clientes externamente
5. **Integridad de precios** — No undercut tarifas publicadas

---

## 19. Puntos de Integración

### Brevo API
- Enviar emails transaccionales
- Trackear opens/clicks (vía dashboard Brevo)
- Gestionar listas de contactos

### Prospect Tracker
- `C:\Users\Usuario\clawd\prospect-tracker.json`
- Leer/escribir estado de prospectos
- Trackear historial de emails

### HEARTBEAT
- `C:\Users\Usuario\clawd\HEARTBEAT.md`
- Referenciar clientes activos para social proof
- Verificar pipeline actual

### Agendar Reuniones
- **Tidycal:** https://tidycal.com/memola/consultoria
- Incluir en todos los emails y CTAs

---

*Memola Medios S.A.S. — Sales Skill v2.0.0 — Febrero 2026*
*"No vendemos horas. Entregamos proyectos que construyen valor."*
