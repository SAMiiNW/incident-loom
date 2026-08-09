from conftest import CONTRACT
import pytest
def test_incident_lifecycle(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy(CONTRACT);direct_vm.sender=direct_alice
    c.open_incident('INC-1','Revocation lag','Identity','SEV-1','Revocation propagation exceeds thirty seconds across two regions.',['priority lane enabled'],['stale sessions'],'restore normal lane after drain')
    assert c.get_summary()['incidents']==1
    direct_vm.mock_llm(r'.*IncidentLoom.*','{"outcome":"WATCH","risk":"HIGH","missing_evidence":[],"required_actions":["verify drain"],"confidence":80,"summary":"Containment is progressing."}')
    c.assess_incident('INC-1');assert c.get_assessment('INC-1')['outcome']=='CONTAIN'
    assert c.get_assessment('INC-1')['proof'].startswith('0x494c')

def test_rejects_bad_input_and_duplicates(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy(CONTRACT);direct_vm.sender=direct_alice
    with pytest.raises(Exception):c.open_incident('bad','Bad','','SEV-9','This report is deliberately long enough to pass length. ',[],[],'')
    c.open_incident('INC-X','Valid incident','Identity','SEV-2','This report is deliberately long enough to pass length. ',[],[],'')
    with pytest.raises(Exception):c.open_incident('INC-X','Duplicate','Identity','SEV-2','This report is deliberately long enough to pass length. ',[],[],'')

def test_unknown_model_risk_is_normalized(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy(CONTRACT);direct_vm.sender=direct_alice
    c.open_incident('INC-R','Risk normalization','Identity','SEV-2','This report describes a multi-region session failure. ',[],[],'')
    direct_vm.mock_llm(r'.*IncidentLoom.*','{"outcome":"WATCH","risk":"UNKNOWN_VALUE","missing_evidence":[],"required_actions":[],"confidence":60,"summary":"Watch closely."}')
    c.assess_incident('INC-R');assert c.get_assessment('INC-R')['risk']=='HIGH'
    with pytest.raises(Exception):c.assess_incident('INC-R')
