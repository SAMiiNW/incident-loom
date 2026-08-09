# INCIDENTLOOM // FIELD DOSSIER

> The alert is not the incident. The evidence is.

IncidentLoom is a dark-room command surface for responders operating while the facts are still moving. It preserves the first observable signals, the containment action, the known risk, and the recovery route as a single immutable incident record. GenLayer validators act as an independent council: they read the same evidence and decide what the situation actually demands.

**Live command wall:** https://incident-loom.pages.dev

## Situation board

```text
SIGNAL CAPTURED
      │
      ▼
EVIDENCE SEALED ──────► BRADBURY
      │
      ▼
VALIDATOR COUNCIL
      │
      ├── STABLE
      ├── WATCH
      ├── CONTAIN
      └── ESCALATE
```

The interface is deliberately built like an operations room rather than a form dashboard: a live incident feed on the left, a chronological situation spine in the center, and a blast/containment rail on the right.

## What the council writes

Every assessment returns a structured operational verdict:

- outcome and normalized risk;
- confidence score;
- likely failure domain;
- ordered containment actions;
- missing evidence;
- short decision rationale;
- an on-chain hexadecimal proof reference.

The model does not get the final word alone. Deterministic contract rules reject invalid severity values, prevent duplicate incidents, allow only the incident owner to request assessment, normalize unknown risk to `HIGH`, and block a second verdict for the same incident.

## Live deployment

| Field | Value |
|---|---|
| Network | GenLayer Bradbury Testnet |
| Chain ID | `4221` |
| Contract | `0xcd9d3324d0d3a524CEF16184e6e58841bd58423F` |
| Live app | https://incident-loom.pages.dev |
| Deployer | `0xCAFA30BF94D4fb01146588a1b7901BD85E7DbD0f` |
| Explorer | [Bradbury Explorer](https://explorer-bradbury.genlayer.com/) |

## Operator procedure

Open the command wall, connect Rabby or MetaMask, then choose **Open incident**. Record a concise title, affected service, direct observation, known risk, the action already taken, and a recovery path. Sealing the incident is one wallet transaction. Requesting the council verdict is a separate, explicit transaction.

Keep the page open while the validator council reaches agreement. IncidentLoom never submits a replacement transaction behind the operator's back: it keeps the original hash and polls its receipt at a controlled interval.

## Contract interface

```python
open_incident(...)
assess_incident(incident_id)
get_incident(incident_id)
get_assessment(incident_id)
get_incidents_page(offset, limit)
get_summary()
```

## Verification record

The contract suite covers normal response flow plus hostile and malformed cases:

```bash
python -m pytest -q
# 3 passed
```

The production interface is also type-checked and statically exported:

```bash
cd frontend
npm install
npm run build
```

## Local command wall

```bash
cd frontend
npm run dev -- -p 3101
```

Visit `http://localhost:3101`. Wallet connection automatically requests Bradbury when required.

## Repository map

- `contracts/contract.py` — incident state machine and validator council logic
- `tests/direct/` — lifecycle, authorization, normalization, and replay tests
- `frontend/app/` — command-wall composition, motion, progress, and error states
- `frontend/lib/chain.ts` — wallet, Bradbury reads, single-submit writes, receipt tracking
- `scripts/deploy.py` — SAMiiNW Bradbury deployment path

IncidentLoom is not an observability clone and it does not pretend to replace responders. It creates a durable boundary between what an operator observed, what validators concluded, and what the chain can prove.
