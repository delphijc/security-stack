## note need to install "pip install flask requests"

import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- CONFIGURATION (Env vars or placeholders) ---
GPU_NODE_URL = os.getenv("GPU_NODE_URL", "http://gpu-node:5000/summarize")
OPENCTI_URL = os.getenv("OPENCTI_URL", "http://opencti:4000/graphql")
RL_POLICY_URL = os.getenv("RL_POLICY_URL", "http://rl-policy-service:8080/recommend")
ELASTIC_URL = os.getenv("ELASTIC_URL", "https://elastic-siem:5601/api/cases")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY", "your_secret_api_key")

@app.route('/siem-webhook', methods=['POST'])
def handle_siem_alert():
    try:
        # ---------------------------------------------------------
        # Step 1: Parse the alert payload
        # ---------------------------------------------------------
        payload = request.json
        if not payload:
            return jsonify({"error": "No JSON payload received"}), 400

        # Extract relevant data (Mocking standard Elastic Alert schema)
        alert_id = payload.get('id', 'unknown_id')
        log_message = payload.get('message', '')
        source_ip = payload.get('source_ip', None)
        
        print(f"[*] Received Alert ID: {alert_id}")

        # ---------------------------------------------------------
        # Step 2: Send log message to `gpu-node` (/summarize endpoint)
        # ---------------------------------------------------------
        ai_summary = "Summary unavailable"
        try:
            print(f"[*] Requesting summary from GPU Node...")
            # Assuming gpu-node expects {"text": "raw log"}
            gpu_response = requests.post(GPU_NODE_URL, json={"text": log_message}, timeout=5)
            if gpu_response.status_code == 200:
                ai_summary = gpu_response.json().get('summary', 'No summary key in response')
        except requests.exceptions.RequestException as e:
            print(f"[!] GPU Node Error: {e}")

        # ---------------------------------------------------------
        # Step 3: Query OpenCTI for related IOCs
        # ---------------------------------------------------------
        opencti_intelligence = {}
        if source_ip:
            try:
                print(f"[*] Querying OpenCTI for IP: {source_ip}...")
                # Mocking a query - Real implementation requires GraphQL query string
                cti_payload = {
                    "query": f"query {{ indicator(value: \"{source_ip}\") {{ confidence label }} }}"
                }
                cti_response = requests.post(OPENCTI_URL, json=cti_payload, timeout=5)
                if cti_response.status_code == 200:
                    opencti_intelligence = cti_response.json().get('data', {})
            except requests.exceptions.RequestException as e:
                print(f"[!] OpenCTI Error: {e}")

        # ---------------------------------------------------------
        # Step 4: (Optional) Query RL Policy service for recommended action
        # ---------------------------------------------------------
        recommended_action = "Manual Investigation Required"
        try:
            print(f"[*] Querying RL Policy Service...")
            rl_payload = {
                "alert_type": payload.get('rule', {}).get('name'),
                "severity": payload.get('severity'),
                "ai_summary": ai_summary,
                "threat_intel": opencti_intelligence
            }
            rl_response = requests.post(RL_POLICY_URL, json=rl_payload, timeout=3)
            if rl_response.status_code == 200:
                recommended_action = rl_response.json().get('action', recommended_action)
        except requests.exceptions.RequestException as e:
             print(f"[!] RL Policy Error: {e}")

        # ---------------------------------------------------------
        # Step 5: Update Elastic SIEM case with summary and recommendation
        # ---------------------------------------------------------
        update_success = False
        try:
            print(f"[*] Updating Elastic SIEM Case...")
            
            # Formulate the comment or case update body
            case_update_body = {
                "comment": (
                    f"**AI Automated Triage**\n\n"
                    f"**Summary:** {ai_summary}\n"
                    f"**OpenCTI Intel:** {opencti_intelligence}\n"
                    f"**Recommended Action:** {recommended_action}"
                )
            }
            
            headers = {
                "Authorization": f"ApiKey {ELASTIC_API_KEY}",
                "Content-Type": "application/json",
                "kbn-xsrf": "true" # Required for Kibana APIs
            }

            # Assuming we are attaching a comment to a specific case related to this alert
            # In a real scenario, you might need to 'Find' the case ID via the Alert ID first
            elastic_endpoint = f"{ELASTIC_URL}/{alert_id}/comments" 
            
            siem_response = requests.post(elastic_endpoint, headers=headers, json=case_update_body, timeout=10)
            if siem_response.status_code in [200, 201]:
                update_success = True
                print("[*] Elastic Case updated successfully.")
            else:
                print(f"[!] Elastic Update Failed: {siem_response.status_code} - {siem_response.text}")

        except requests.exceptions.RequestException as e:
            print(f"[!] Elastic Connection Error: {e}")

        return jsonify({
            "status": "processed",
            "ai_summary": ai_summary,
            "recommended_action": recommended_action,
            "elastic_updated": update_success
        }), 200

    except Exception as e:
        print(f"[!!!] Critical Application Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)