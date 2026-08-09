# IncidentLoom

IncidentLoom is an on-chain incident command system for turning incomplete operational evidence into a validator-backed containment decision. Responders record the observable situation, the action already taken, known risks, and a recovery path. Independent GenLayer validators then classify the incident and write the council result on-chain.

## Why GenLayer

Operational incidents are described in human language and rarely fit deterministic rules. IncidentLoom uses an Intelligent Contract to let validators interpret the same normalized evidence packet independently, while deterministic guards enforce ownership, immutable reports, bounded inputs, valid states, and one assessment per incident.

## Workflow

1. Connect a wallet on GenLayer Bradbury Testnet.
2. Seal an incident with a service, observation, risk, action, and recovery path.
3. Request a council assessment.
4. Validators return an outcome, risk level, confidence, failure domain, required actions, and rationale.
5. The result and its proof reference remain readable on-chain.

## Contract

- Network: GenLayer Bradbury Testnet (`4221`)
- Address: `0xcd9d3324d0d3a524CEF16184e6e58841bd58423F`
- Core methods: `open_incident`, `assess_incident`, `get_incident`, `get_assessment`, `get_incidents_page`, `get_summary`
- Explorer: https://explorer-bradbury.genlayer.com/

The contract normalizes validator output and applies deterministic safety checks after consensus. Unknown risk values are converted to `HIGH`, invalid severities are rejected, duplicate IDs are prevented, and proof identifiers are valid hexadecimal values.

## Run locally

```bash
cd frontend
npm install
npm run dev -- -p 3101
```

Open http://localhost:3101 and connect Rabby or MetaMask. The app can add and switch to Bradbury automatically.

## Tests

```bash
python -m pytest -q
cd frontend
npm run build
```

The contract suite covers the complete lifecycle, invalid and duplicate inputs, risk normalization, proof format, and repeated-assessment protection.

## Structure

```text
contracts/   Intelligent Contract
frontend/    Next.js command interface
scripts/     Bradbury deployment script
tests/       Contract and adversarial tests
```

## Safety model

Wallet submission happens once per action. Receipt polling never resubmits the transaction, busy states prevent double clicks, and contract execution rollbacks are surfaced explicitly.

