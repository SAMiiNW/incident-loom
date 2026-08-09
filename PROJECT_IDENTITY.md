# IncidentLoom

## Product
An on-chain incident command system where responders submit live situation packets and GenLayer validators independently classify severity, likely failure domain, containment priority, and whether the evidence justifies escalation.

## Why GenLayer
Incident evidence is incomplete, textual, and often contradictory. A normal smart contract cannot interpret logs, symptoms, user impact, and responder notes. GenLayer consensus becomes the neutral incident council rather than trusting one operator or one AI API.

## Intelligent Contract
- Entities: workspaces, incidents, situation reports, council decisions, containment actions.
- Core write: `assess_incident(incident_id)`.
- Consensus output: severity, failure_domain, confidence band, containment order, escalation flag, concise rationale.
- Gates: OBSERVE, CONTAIN, ESCALATE, RECOVER, CLOSE.
- Deterministic protections: owner/member roles, bounded text, immutable reports, pagination, valid state transitions, duplicate checks.
- Validation: validators independently analyze a compact normalized packet; agreement requires severity and gate match with compatible failure domain.

## Frontend
- Composition: asymmetric command wall, vertical event spine, blast-radius matrix, containment rail.
- Palette: carbon `#090b0d`, oxidized amber `#d58a2a`, signal orange `#ff5a2f`, cold white `#e9eef0`.
- Type: condensed grotesk display, technical mono telemetry.
- Motion: scanner sweep, snapping incident cards, ticking elapsed time, controlled alert pulse.
- Skeleton: blueprint boxes drawn by a diagnostic beam; no shimmer cards.
- Empty state: animated dormant waveform with a single “Open incident” control.
- Transaction progress: full-width incident transmission strip with signed, activated, council, committed states.

## Non-overlap
Not a software proposal runway, story game, archive, market, or generic dashboard. Its primary artifact is a time-sensitive incident timeline and containment decision.
