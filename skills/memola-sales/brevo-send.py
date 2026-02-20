#!/usr/bin/env python3
"""
Memola Medios S.A.S. — Brevo Email Sender
Sends personalized sales emails via Brevo API
Project-based service model (v2.0)
"""

import requests
import json
import sys
from datetime import datetime

# Brevo Configuration — Set BREVO_API_KEY environment variable
import os
BREVO_API_KEY = os.environ.get("BREVO_API_KEY", "")
FROM_EMAIL = os.environ.get("BREVO_FROM_EMAIL", "agencia@memola.media")
FROM_NAME = os.environ.get("BREVO_FROM_NAME", "Memola Medios S.A.S.")
API_ENDPOINT = "https://api.brevo.com/v3/smtp/email"

if not BREVO_API_KEY:
    print("Warning: BREVO_API_KEY environment variable not set")

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "api-key": BREVO_API_KEY
}


def send_email(to_email: str, subject: str, body: str, tags: list = None) -> dict:
    """
    Send email via Brevo API

    Args:
        to_email: Recipient email address
        subject: Email subject line
        body: Plain text email body
        tags: List of tags for tracking

    Returns:
        dict with success status and message_id or error
    """

    payload = {
        "sender": {
            "name": FROM_NAME,
            "email": FROM_EMAIL
        },
        "to": [{"email": to_email}],
        "subject": subject,
        "textContent": body,
        "tags": tags or ["Memola Sales"]
    }

    try:
        response = requests.post(API_ENDPOINT, headers=HEADERS, json=payload)

        if response.status_code == 201:
            result = response.json()
            return {
                "success": True,
                "message_id": result.get("messageId"),
                "timestamp": datetime.now().isoformat()
            }
        else:
            return {
                "success": False,
                "error": f"HTTP {response.status_code}: {response.text}",
                "timestamp": datetime.now().isoformat()
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


def send_discovery_email(prospect: dict) -> dict:
    """
    Send discovery email to a prospect (project-based model)

    Args:
        prospect: dict with company, sector, city, email, discovery_question
    """

    subject = f"Pregunta: ¿{prospect['company']} y presencia digital?"

    body = f"""Hola,

Soy José de Memola Medios. Trabajamos con empresas del NEA que están profesionalizando su presencia digital.

Notamos que {prospect['company']} podría beneficiarse de:

- Sitio web profesional con captura de leads
- Email corporativo (@empresa.com.ar)
- {prospect.get('discovery_question', 'Analytics para medir resultados')}

Tenemos un paquete de entrada desde AR$ 500.000 + IVA que incluye web + email corporativo.

¿Le interesa una consultoría de 15 minutos?

Agendar: https://tidycal.com/memola/consultoria

Saludos desde Mercedes,

José Barnetche
Memola Medios S.A.S.
agencia@memola.media
WhatsApp: +54 9 3773 418130
"""

    tags = ["Discovery", prospect['city'], prospect['sector']]

    return send_email(prospect['email'], subject, body, tags)


def send_followup_email(prospect: dict) -> dict:
    """
    Send follow-up email with Bundle Fundación offer
    """

    subject = f"Seguimiento: Presencia Digital para {prospect['company']}"

    body = f"""Hola,

Hace unos días le escribí sobre la presencia digital de {prospect['company']}.

Quería compartir nuestra oferta de entrada:

BUNDLE FUNDACIÓN — AR$ 650.000 + IVA

Incluye:
- Sitio web one-page responsive
- Email corporativo (hasta 10 casillas)
- Google Analytics configurado

Delivery: 2-4 semanas
Pago: 30% seña / 70% al finalizar

¿Le interesa una consultoría de 15 minutos?

Agendar: https://tidycal.com/memola/consultoria

O puede escribirme directo:
WhatsApp: +54 9 3773 418130

Saludos,
José Barnetche
Memola Medios S.A.S.
"""

    tags = ["Follow-up", "Fundación", prospect['city']]

    return send_email(prospect['email'], subject, body, tags)


def send_upsell_email(client: dict) -> dict:
    """
    Send upsell email to existing client

    Args:
        client: dict with company, project_delivered, weeks, upsell_service, upsell_price
    """

    subject = f"{client['company']}: Siguiente paso para crecer"

    body = f"""Hola,

Completamos {client['project_delivered']} hace {client['weeks']} semanas.

Basado en los resultados, creo que {client['company']} está listo para el siguiente nivel:

{client['upsell_service']}
Inversión: AR$ {client['upsell_price']} + IVA

¿Tiene 15 minutos esta semana para conversarlo?

Agendar: https://tidycal.com/memola/consultoria

Saludos,
José Barnetche
Memola Medios S.A.S.
"""

    tags = ["Upsell", client.get('level', 'General')]

    return send_email(client['email'], subject, body, tags)


def send_proposal_email(prospect: dict) -> dict:
    """
    Send proposal summary email

    Args:
        prospect: dict with company, email, services (list), total_price, payment_terms
    """

    services_list = "\n".join([f"- {s}" for s in prospect['services']])

    subject = f"Propuesta para {prospect['company']}"

    body = f"""Hola,

Gracias por la conversación. Adjunto el resumen de la propuesta:

SERVICIOS PROPUESTOS:
{services_list}

INVERSIÓN TOTAL: AR$ {prospect['total_price']} + IVA

FORMA DE PAGO:
{prospect['payment_terms']}

El siguiente paso es confirmar para agendar el kickoff.

¿Alguna pregunta o ajuste necesario?

Saludos,
José Barnetche
Memola Medios S.A.S.
agencia@memola.media
WhatsApp: +54 9 3773 418130
"""

    tags = ["Proposal", prospect.get('level', 'General')]

    return send_email(prospect['email'], subject, body, tags)


def send_custom_email(to_email: str, subject: str, body: str, campaign: str = "Custom") -> dict:
    """
    Send a custom email with specified content
    """

    # Add signature
    full_body = f"""{body}

---
José Barnetche
Memola Medios S.A.S.
agencia@memola.media
WhatsApp: +54 9 3773 418130
Mercedes, Corrientes — Argentina

Agendar consultoría: https://tidycal.com/memola/consultoria
"""

    return send_email(to_email, subject, full_body, [campaign])


# CLI interface for agent use
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python brevo-send.py discovery <json_prospect>")
        print("  python brevo-send.py followup <json_prospect>")
        print("  python brevo-send.py upsell <json_client>")
        print("  python brevo-send.py proposal <json_prospect>")
        print("  python brevo-send.py custom <email> <subject> <body>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "discovery" and len(sys.argv) >= 3:
        prospect = json.loads(sys.argv[2])
        result = send_discovery_email(prospect)
        print(json.dumps(result, indent=2))

    elif command == "followup" and len(sys.argv) >= 3:
        prospect = json.loads(sys.argv[2])
        result = send_followup_email(prospect)
        print(json.dumps(result, indent=2))

    elif command == "upsell" and len(sys.argv) >= 3:
        client = json.loads(sys.argv[2])
        result = send_upsell_email(client)
        print(json.dumps(result, indent=2))

    elif command == "proposal" and len(sys.argv) >= 3:
        prospect = json.loads(sys.argv[2])
        result = send_proposal_email(prospect)
        print(json.dumps(result, indent=2))

    elif command == "custom" and len(sys.argv) >= 5:
        email = sys.argv[2]
        subject = sys.argv[3]
        body = sys.argv[4]
        result = send_custom_email(email, subject, body)
        print(json.dumps(result, indent=2))

    else:
        print("Invalid command or missing arguments")
        sys.exit(1)
