from conftest import CONTRACT
import pytest
def open_valid(c,direct_vm,incident_id='INC-1',severity='SEV-1'):
    direct_vm.mock_web(r'telemetry\.example',{'status':200,'body':'timestamp=2026-08-11T12:00Z region=eu-west revoked_sessions=0 queue_depth=2 signature=ops-key-7'})
    direct_vm.mock_llm(r'Extract authenticated incident telemetry.*','Authenticated telemetry at 2026-08-11T12:00Z reports zero revoked sessions and queue depth two in eu-west, signed by ops-key-7.')
    c.open_incident(incident_id,'Revocation lag','Identity',severity,'Revocation propagation exceeds thirty seconds across two regions.',['priority lane enabled'],['stale sessions'],'restore normal lane after drain',['https://telemetry.example/incident.json'],'Quarantine stale sessions and drain the revocation queue')
def test_incident_lifecycle(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy(CONTRACT);direct_vm.sender=direct_alice
    open_valid(c,direct_vm)
    assert c.get_summary()['incidents']==1
    direct_vm.mock_llm(r'.*IncidentLoom.*','{"outcome":"WATCH","risk":"HIGH","missing_evidence":[],"required_actions":["verify drain"],"confidence":80,"summary":"Containment is progressing."}')
    c.assess_incident('INC-1');assert c.get_assessment('INC-1')['outcome']=='CONTAIN'
    assert c.get_assessment('INC-1')['proof'].startswith('0x494c')

def test_rejects_bad_input_and_duplicates(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy(CONTRACT);direct_vm.sender=direct_alice
    with pytest.raises(Exception):c.open_incident('bad','Bad','','SEV-9','This report is deliberately long enough to pass length. ',[],[],'',[],'')
    open_valid(c,direct_vm,'INC-X','SEV-2')
    with pytest.raises(Exception):c.open_incident('INC-X','Duplicate','Identity','SEV-2','This report is deliberately long enough to pass length. ',[],[],'',['https://telemetry.example/incident.json'],'Quarantine stale sessions and drain the queue')

def test_unknown_model_risk_is_normalized(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy(CONTRACT);direct_vm.sender=direct_alice
    open_valid(c,direct_vm,'INC-R','SEV-2')
    direct_vm.mock_llm(r'.*IncidentLoom.*','{"outcome":"WATCH","risk":"UNKNOWN_VALUE","missing_evidence":[],"required_actions":[],"confidence":60,"summary":"Watch closely."}')
    c.assess_incident('INC-R');assert c.get_assessment('INC-R')['risk']=='HIGH'
    with pytest.raises(Exception):c.assess_incident('INC-R')
