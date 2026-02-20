# Post-Project Upsell Workflow

**Memola Medios S.A.S.**
**Version:** 1.0
**Updated:** Febrero 2026

---

## Philosophy

> Upselling is not about extracting more money.
> It's about identifying the natural next step for a client who succeeded with you.

Good upsells happen when:
1. The previous project delivered real value
2. There's a logical progression in their digital journey
3. The client has capacity (time + budget) for more
4. They trust you enough to go deeper

---

## The Natural Progression Map

```
LEVEL 1                LEVEL 2                LEVEL 3                LEVEL 4
[Fundación]      →     [Optimización]    →    [Amplificación]   →   [Audiovisual]

Website          →     Branding          →    Meta Ads         →    Video
Email corp       →     Landing pages     →    Email Marketing  →    Fotografía
Analytics        →     Funnel audit      →    (Optimization)   →    Eventos
```

### Typical Client Journeys

**Journey A: New Business Building Presence**
```
Bundle Fundación (AR$ 650K)
     ↓ [+4 weeks]
Analytics shows traffic, low conversion
     ↓
Landing page optimization (AR$ 300K-500K)
     ↓ [+8 weeks]
Conversion improved, needs more traffic
     ↓
Meta Ads setup (AR$ 1.21M)
```

**Journey B: Established Business Modernizing**
```
Website redesign (AR$ 1.2M)
     ↓ [+6 weeks]
Client mentions "our logo is old"
     ↓
Rebranding (AR$ 800K-1.5M)
     ↓ [+8 weeks]
Aniversario de empresa
     ↓
Video institucional (AR$ 1.5M-2.5M)
```

**Journey C: Content-First Entry**
```
Sesión fotográfica (AR$ 300K)
     ↓ [+2 weeks]
Client loved the photos, no website
     ↓
Bundle Fundación (AR$ 650K)
     ↓ [+8 weeks]
Needs ongoing content
     ↓
Meta Ads + Email Marketing
```

---

## Post-Project Timeline

### Immediate (Week 0-2)
- Deliver final assets
- Send project completion email
- Confirm client satisfaction
- Request testimonial (if appropriate)

### Short-term (Week 3-6)
- Check-in: "¿Cómo está funcionando?"
- Share any metrics if available (analytics, engagement)
- **Listen for upsell signals**

### Medium-term (Week 8-12)
- Proactive check-in
- Share relevant insight or tip
- **Propose next level if signals detected**

### Long-term (Month 4-6)
- Quarterly touch-base
- Share industry updates
- Keep relationship warm for future needs

---

## Upsell Signal Detection

### Level 1 → Level 2 Signals
| Signal | Interpretation | Upsell |
|--------|----------------|--------|
| "Mi logo se ve viejo en el sitio nuevo" | Visual inconsistency | Rebranding |
| "Las visitas no se convierten en contactos" | Funnel issue | Landing optimization |
| "¿Puedo agregar otra página?" | Growing needs | Multi-page upgrade |
| High bounce rate (>60%) in analytics | UX/content issue | Funnel audit |

### Level 2 → Level 3 Signals
| Signal | Interpretation | Upsell |
|--------|----------------|--------|
| "¿Cómo traigo más tráfico?" | Ready for paid | Meta Ads |
| "Tengo una base de emails pero no los uso" | Nurture opportunity | Email Marketing |
| "Funciona bien pero es poco volumen" | Needs scale | Ads + Email bundle |
| Conversion rate >3% | Foundation solid | Safe to scale |

### Level 3 → Level 4 Signals
| Signal | Interpretation | Upsell |
|--------|----------------|--------|
| "Tenemos un evento importante" | Content opportunity | Cobertura |
| "Cumplimos X años" | Milestone | Video institucional |
| "Necesitamos explicar mejor el producto" | Education gap | Tutoriales |
| "Las fotos del sitio no nos representan" | Visual upgrade | Fotografía |

### General Upsell Signals
- Client proactively reaches out (engaged)
- Mentions competitor doing something
- Business expansion (new location, new product)
- New person joins decision-making (fresh perspective)
- Seasonal peak approaching (preparation time)

---

## Upsell Conversation Templates

### The Check-In Opener
```
Hola [Nombre],

Quería ver cómo está funcionando [proyecto completado] después de [X] semanas.

¿Han notado algún cambio en [métrica relevante]?

Me cuenta cuando tenga un momento.

José
```

### The Signal-Based Pivot
```
Me comentaba que [señal detectada].

Eso es algo que resolvemos con [servicio siguiente].

El ticket sería AR$ [precio] + IVA.

¿Le interesa que le arme una propuesta específica?
```

### The Value-Add Suggestion
```
Mirando los analytics de su sitio, noto que [insight].

En clientes similares, esto se resolvió con [servicio].

No es urgente, pero lo dejo como idea para cuando quieran dar el siguiente paso.
```

### The Direct Upsell (When Asked)
```
Hola [Nombre],

Basado en lo que hicimos con [proyecto anterior], el siguiente paso natural sería [servicio].

Esto incluye:
- [Entregable 1]
- [Entregable 2]
- [Entregable 3]

Inversión: AR$ [precio] + IVA
Delivery: [timeline]

¿Quiere que agendemos para charlar los detalles?
```

---

## Upsell Email via Brevo

Use `send_upsell_email()` function:

```python
client = {
    "company": "Empresa S.A.",
    "email": "cliente@empresa.com",
    "project_delivered": "el sitio web",
    "weeks": 6,
    "upsell_service": "Meta Ads Setup — 4 campañas configuradas, píxel instalado, cuenta lista",
    "upsell_price": "1.210.000",
    "level": "Level3"
}

send_upsell_email(client)
```

---

## When NOT to Upsell

### Red Flags
- Client was difficult during project
- Payment was late or problematic
- Project went over scope/timeline
- Client hasn't used what you delivered
- Previous project didn't achieve goals

### Context Situations
- Client in crisis mode (focus on stability)
- Recent negative feedback (fix relationship first)
- Too soon after delivery (let them breathe)
- Wrong timing (budget cycle, vacation, emergency)

### The "Not Now" Response
If client says "not now":
1. Acknowledge: "Entiendo perfectamente"
2. Leave door open: "Cuando estén listos, me avisa"
3. Note in CRM: "Upsell declined - [reason] - revisit [date]"
4. Continue relationship maintenance

---

## Tracking Upsells

### Metrics to Track
| Metric | Target |
|--------|--------|
| Upsell conversation rate | >30% of clients |
| Upsell close rate | >20% of conversations |
| Time to upsell | 6-12 weeks post-project |
| Average upsell ticket | >AR$ 800.000 |
| Client lifetime value | 2x initial project |

### CRM Fields for Upsell Tracking
- `last_project_date`
- `last_project_value`
- `upsell_potential` (Low/Medium/High)
- `upsell_signals` (notes)
- `next_upsell_date`
- `upsell_attempts`

---

## Client Segmentation for Upsells

### High Potential (Prioritize)
- Paid on time
- Project delivered smoothly
- Gave positive feedback
- Business is growing
- Has budget authority
- Multiple business units

### Medium Potential (Standard)
- Project was OK
- No complaints
- Stable business
- Some growth potential
- May need approval

### Low Potential (Maintain Only)
- Difficult project
- Price-sensitive
- Single-product business
- No growth signals
- Committee decisions

---

## Integration with VIGIL

### Post-Project VIGIL Update
After project completion, update VIGIL qualification:

```
CLIENT HEALTH CHECK — [Company]
Date: [YYYY-MM-DD]

ORIGINAL VIGIL SCORE: [X/5]

PROJECT DELIVERED: [Description]
VALUE: AR$ [Amount]
STATUS: [Successful/Partial/Problematic]

UPSELL POTENTIAL: [High/Medium/Low]
NEXT SERVICE: [Recommendation]
ESTIMATED TICKET: AR$ [Amount]

RELATIONSHIP QUALITY: [Excellent/Good/OK/Poor]

NEXT ACTION: [Specific action + date]
```

---

*Remember: The best upsells feel like helpful suggestions, not sales pitches.*
*If you're not sure the client would benefit, don't propose it.*
