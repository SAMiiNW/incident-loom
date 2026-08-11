import json, os, re, time
from genlayer_py import create_client, create_account
from genlayer_py.chains import testnet_bradbury

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKSPACE=os.path.abspath(os.path.join(ROOT,'..','..','..','..'))
def value(name):
    text=open(os.path.join(WORKSPACE,'accounts.env'),encoding='utf-8').read()
    return re.search(rf'^\s*{name}\s*=\s*"?([^"\r\n]+)',text,re.M).group(1).strip()
def wait(c,h): return c.wait_for_transaction_receipt(transaction_hash=h,status='ACCEPTED',retries=60,interval=30000)
def main():
    account=create_account(account_private_key=value('ACCOUNT_1_GENLAYER_PRIVATE_KEY'))
    client=create_client(chain=testnet_bradbury,account=account)
    address=json.load(open(os.path.join(ROOT,'deployment.json'),encoding='utf-8'))['contract']
    incident='AUDIT-'+str(int(time.time()))
    args=[incident,'Public API availability review','Edge API','SEV-2','Operators observed elevated request failures and need an evidence-bound containment decision.',['Paused nonessential writes'],['Stale client sessions may retry'], 'Restore traffic gradually after the public status feed reports recovery.',['https://www.cloudflarestatus.com/api/v2/status.json'],'Keep nonessential writes paused and route affected traffic to the healthy region until telemetry confirms recovery.']
    opened=client.write_contract(address=address,function_name='open_incident',args=args); print('openTx',opened,flush=True); wait(client,opened)
    assessed=client.write_contract(address=address,function_name='assess_incident',args=[incident]); print('assessTx',assessed,flush=True); wait(client,assessed)
    print(json.dumps({'incidentId':incident,'openTx':opened,'assessTx':assessed,'status':'ACCEPTED'},indent=2),flush=True)
if __name__=='__main__': main()
