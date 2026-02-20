# Discovery to Proposal Workflow

**Memola Medios S.A.S.**
**Version:** 1.0
**Updated:** Febrero 2026

---

## Overview

```
LEAD SOURCE → QUALIFICATION → DISCOVERY CALL → PROPOSAL → CLOSE
```

---

## Step 1: Lead Source & Initial Contact

### Sources
| Source | Action | Response Time |
|--------|--------|---------------|
| TidyCal booking | Confirm call | Automático |
| WhatsApp directo | Qualify, propose call | < 4 horas |
| Email frío response | Qualify, propose call | < 24 horas |
| Referido de cliente | Priority qualify | < 2 horas |
| VIGIL sweep | Discovery email | Batch weekly |

### Initial Qualification (Pre-Call)
Before scheduling discovery call, verify:
- [ ] Sector fits MEMOLA terrain (no startups, no urgency-driven)
- [ ] Estimated revenue > AR$ 50M/año
- [ ] Decision maker identified
- [ ] Budget appears viable (> AR$ 300.000)

**If NO on any:** Politely decline or refer elsewhere.

---

## Step 2: Discovery Call (15 min)

### Agenda
```
[0-2 min]  Intro + rapport
[2-8 min]  Discovery questions
[8-12 min] Pain points + priorities
[12-15 min] Next steps + timeline
```

### Discovery Questions by Intent

**For new digital presence:**
- "¿Cómo los encuentra un cliente nuevo actualmente?"
- "¿Qué porcentaje viene por referido vs búsqueda?"
- "¿Tienen email corporativo o usan Gmail/Hotmail?"

**For scaling existing presence:**
- "¿Cuántas visitas mensuales tiene el sitio actual?"
- "¿Qué porcentaje convierte en contacto/venta?"
- "¿Han probado publicidad paga antes?"

**For content/audiovisual:**
- "¿Qué contenido les gustaría tener que no tienen hoy?"
- "¿Tienen evento, aniversario, o lanzamiento próximo?"
- "¿Cómo usan el contenido actualmente? (Web, redes, presentaciones)"

### Qualifying Questions (Must Ask)
1. "¿Quién toma la decisión final sobre este tipo de inversión?"
2. "¿Tienen presupuesto asignado o estamos explorando posibilidades?"
3. "¿Cuál es el timeline ideal para tener esto funcionando?"

### Red Flags During Call
- "Solo estoy cotizando para comparar" → No enviar propuesta
- "Necesitamos esto para ayer" → Sprint terrain, decline
- "Mi socio/jefe tiene que aprobarlo" → Pedir call con decision maker
- No puede describir el pain point → Not ready

---

## Step 3: Post-Call Assessment

### VIGIL Scoring (Apply Within 24h)
```
TERRAIN SCORE: [X/5]
1. Sobrevivir largo plazo: [SÍ/NO]
2. Erosión vs explosión: [SÍ/NO]
3. Legitimidad > velocidad: [SÍ/NO]
4. Claridad impacta: [SÍ/NO]
5. Sin viralidad: [SÍ/NO]
```

**Decision:**
- 5/5 → PROCEED — Full proposal
- 4/5 → PROCEED — Standard proposal
- 3/5 → CAUTION — Level 1 only, simple scope
- 0-2/5 → DECLINE — Send polite no

### Service Level Determination

| Client Situation | Recommended Level | Entry Point |
|------------------|-------------------|-------------|
| No digital presence | Level 1 | Bundle Fundación AR$ 650K |
| Basic presence, low conversion | Level 2 | Funnel audit AR$ 400K |
| Presence OK, needs traffic | Level 3 | Meta Ads AR$ 1.21M |
| Needs premium content | Level 4 | Varies by scope |
| Multiple needs | Multi-level | Custom proposal |

---

## Step 4: Proposal Preparation

### Timeline
- Simple (Level 1): Send within 48 horas
- Complex (Multi-level): Send within 5 días hábiles

### Proposal Components
1. **Context recap** — What they said, what we understood
2. **Recommended services** — Specific to their needs
3. **Pricing** — Clear breakdown + totals
4. **Timeline** — Realistic delivery dates
5. **Payment terms** — Per standard structure
6. **Next steps** — What happens when they say yes

### Use Templates
- Level 1: `templates/proposals/level-1-fundacion.md`
- Level 2: `templates/proposals/level-2-optimizacion.md`
- Level 3: `templates/proposals/level-3-amplificacion.md`
- Level 4: `templates/proposals/level-4-audiovisual.md`

### Sending the Proposal
**Method:** Email via Brevo (send_proposal_email)

**Subject:** "Propuesta para [Company]"

**Body structure:**
- Greeting
- Summary of conversation
- Link to full proposal (PDF or doc)
- Clear CTA
- Signature with WhatsApp

---

## Step 5: Follow-Up Sequence

### Timeline
| Day | Action |
|-----|--------|
| 0 | Send proposal |
| +3 | WhatsApp check-in |
| +7 | Email follow-up (if no response) |
| +14 | Final follow-up |
| +21 | Archive if no response |

### Follow-Up Templates

**Day +3 (WhatsApp):**
```
Hola [Nombre], soy José de Memola.
¿Pudo revisar la propuesta que le envié?
Cualquier duda me avisa.
```

**Day +7 (Email):**
```
Subject: Seguimiento: Propuesta [Company]

Hola,

Quería saber si tuvo oportunidad de revisar la propuesta.

Si tiene dudas o necesita ajustes, con gusto conversamos.

¿Le parece coordinar una llamada breve?

Saludos,
José
```

**Day +14 (Final):**
```
Subject: Última consulta - Propuesta [Company]

Hola,

Entiendo que quizás no sea el momento adecuado.

Si en el futuro necesita apoyo con presencia digital,
quedo a disposición.

Saludos,
José
```

---

## Step 6: Closing

### When They Say Yes
1. Enviar factura de seña (30%)
2. Confirmar recepción de pago
3. Agendar kickoff call
4. Crear carpeta de proyecto
5. Enviar brief/onboarding form

### When They Say No
1. Agradecer el tiempo
2. Preguntar (opcional): "¿Puedo preguntar qué influyó en la decisión?"
3. Marcar en CRM como "Declined - [Reason]"
4. Agregar a nurture list (contactar en 6 meses)

### When They Ghost
1. Después de Day +21 sin respuesta
2. Marcar como "No Response"
3. No agregar a nurture (no mostraron intent)
4. Liberar mental bandwidth

---

## CRM/Tracking

### Prospect Status
| Status | Meaning |
|--------|---------|
| `lead` | Initial contact, not qualified |
| `qualified` | Passed VIGIL, awaiting call |
| `discovery` | Call scheduled or completed |
| `proposal_sent` | Proposal delivered |
| `negotiating` | Active discussion on scope/price |
| `won` | Signed + seña received |
| `lost` | Declined or no response |

### Required Fields
- Company name
- Contact name + email
- Sector
- City
- VIGIL score
- Service level proposed
- Ticket value
- Status
- Last activity date

---

## Automation via Brevo

### Available Functions
```python
send_discovery_email(prospect)   # Initial outreach
send_followup_email(prospect)    # Day +7 follow-up
send_proposal_email(prospect)    # Proposal delivery
send_custom_email(email, subject, body, campaign)
```

### Tags for Tracking
- `Discovery` — Initial outreach
- `Follow-up` — Post-discovery
- `Proposal` — Proposal sent
- `Won` — Client closed
- `Lost` — Did not proceed

---

*Workflow designed for foundation-terrain clients.*
*No spam. No pressure. Professional persistence.*
